from book.api.serializer import FlightReservationSerializer, HotelRoomReservationSerializer, VillaReservationSerializer
from rest_framework import mixins, viewsets
from book.models import FlightReservation, HotelRoomReservation, VillaReservation
from filtering.filter import HotelRoomReservationFilterSet, VillaReservationFilterSet


class FlightReservationViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    queryset = FlightReservation.objects.all()
    serializer_class = FlightReservationSerializer


class HotelRoomReservationViewSet(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  viewsets.GenericViewSet):
    queryset = HotelRoomReservation.objects.all()
    serializer_class = HotelRoomReservationSerializer
    filterset_class = HotelRoomReservationFilterSet


class VillaReservationViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    queryset = VillaReservation.objects.all()
    serializer_class = VillaReservationSerializer
    filterset_class = VillaReservationFilterSet
