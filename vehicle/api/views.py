from vehicle.api.serializer import FlightSerializer
from rest_framework import mixins, viewsets
from vehicle.models import Flight
from filtering.filter import FightFilterset


class FlightViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filterset_class = FightFilterset
