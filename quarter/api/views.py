from quarter.api.serializer import VillaSerializer, HotelSerializer, HotelRoomSerializer
from rest_framework import mixins, viewsets
from quarter.models import Villa, Hotel, HotelRoom
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
