from rest_framework import serializers
from .models import *


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('title', 'origin', 'destination', 'price', 'company', 'arrive_time',
                  'depart_time', 'category', 'capacity', 'flight_type', 'gate', 'airplane_type', 'is_valid', )
