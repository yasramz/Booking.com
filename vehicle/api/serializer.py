from rest_framework import serializers
from vehicle.models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'title', 'origin', 'destination', 'price', 'company', 'arrive_time',
                  'depart_time', 'category', 'capacity', 'flight_type', 'airplane_type', 'is_valid', )


class FlightRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlightRate
        fields = ('id', 'hotel', 'user', 'rate',)


class FlightCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightComment
        fields = ('id', 'parent', 'comment_body', 'status', 'hotel', 'user', )

    extra_kwarg = {
        'parent': {'required': False},
        'status': {'read_only': True},
    }
