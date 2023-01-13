from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from vehicle.api.serializer import *
from rest_framework import mixins, viewsets
from vehicle.models import Flight
from filtering.filter import FightFilterset


class FlightViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filterset_class = FightFilterset


class FlightRateViewSet(mixins.CreateModelMixin,
                        # mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = FlightRateSerializer
    queryset = FlightRate.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class FlightCommentViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = FlightCommentSerializer
    queryset = FlightComment.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
