from vehicle.api.serializer import FlightSerializer
from rest_framework import mixins, viewsets
from vehicle.models import Flight


class FlightViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
