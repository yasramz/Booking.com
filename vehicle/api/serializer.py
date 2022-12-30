from rest_framework import serializers
from vehicle.models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('title', 'origin', 'destination', 'price', 'company', 'arrive_time',
                  'depart_time', 'category', 'capacity', 'flight_type', 'airplane_type', 'is_valid', )
