from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from quarter.api.serializer import *
from rest_framework import mixins, viewsets
from quarter.models import *
from filtering.filter import VillaFilterSet, HotelRoomFilterSet


class VillaViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    filterset_class = VillaFilterSet


class HotelViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRoomViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    filterset_class = HotelRoomFilterSet


class HotelCommentViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = HotelCommentSerializer
    queryset = HotelComment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class HotelRoomCommentViewSet(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = HotelRoomCommentSerializer
    queryset = HotelRoomComment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class VillaCommentViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = VillaCommentSerializer
    queryset = VillaComment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class HotelRateViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = HotelRateSerializer
    queryset = HotelRate.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class HotelRoomRateViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = HotelRoomSerializer
    queryset = HotelRoomRate.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class VillaRateViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = VillaRateSerializer
    queryset = HotelComment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]
