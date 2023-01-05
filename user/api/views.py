from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.api.serializer import UserSerializer, BankInfoSerializer, ProfileSerializer, StepOneLoginSerializer, StepTwoLoginSerializer
from user.models import User, Profile, BankInfo
from utils.utils import get_tokens_for_user, generate_otp


class ProfileViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all().prefetch_related('user', 'bank_info')
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet
):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        elif self.action == 'list':
            return [IsAdminUser()]


class LoginStepOneAPIView(GenericAPIView):
    serializer_class = StepOneLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data['email']
            code = generate_otp()
            cache.set(str(email), code, 120)

            return Response({"code": code})


class LoginStepTwoAPIView(GenericAPIView):
    serializer_class = StepTwoLoginSerializer

    def post(self, request):
        email = request.data['email']
        user_answer = request.data['code']
        code = cache.get(str(email))

        if user_answer == code:
            try:
                user = User.objects.get(email=email)
                tokens = get_tokens_for_user(user)
                return Response(tokens)

            except ObjectDoesNotExist:
                return Response('no user with this email address!')

        else:
            return Response('Code does not match!')
