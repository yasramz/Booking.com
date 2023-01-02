from book.api.serializer import FlightReservationSerializer, HotelRoomReservationSerializer, VillaReservationSerializer
from rest_framework import mixins, viewsets
from book.models import FlightReservation, HotelRoomReservation, VillaReservation


class FlightReservationViewSet(mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = FlightReservation.objects.all()
    serializer_class = FlightReservationSerializer


class HotelRoomReservationViewSet(mixins.RetrieveModelMixin,
                                  mixins.ListModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    queryset = HotelRoomReservation.objects.all()
    serializer_class = HotelRoomReservationSerializer


class VillaReservationViewSet(mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    queryset = VillaReservation.objects.all()
    serializer_class = VillaReservationSerializer
