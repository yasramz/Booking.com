from quarter.api.serializer import VillaSerializer, HotelSerializer, HotelRoomSerializer
from rest_framework import mixins, viewsets
from quarter.models import Villa, Hotel, HotelRoom


class VillaViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Villa.objects.all()
    serializer_class = VillaSerializer


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
