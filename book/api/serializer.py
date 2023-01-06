from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from book.models import *
from vehicle.api.serializer import FlightSerializer
from quarter.api.serializer import HotelRoomSerializer, VillaSerializer
from user.api.serializer import UserSerializer
from vehicle.models import Flight


class FlightReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlightReservation
        fields = ('user', 'airplane')

    def create(self, validated_data):
        flight = Flight.objects.get(id=validated_data['airplane'].id)

        if flight.capacity > 0:
            flight.capacity = flight.capacity - 1
            flight.save()
            return super(FlightReservationSerializer, self).create(validated_data)
        else:
            raise ObjectDoesNotExist('No sit available')


class HotelRoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomReservation
        fields = ('user', 'check_in', 'check_out', 'hotel_room')

    def create(self, validated_data):
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']

        case_1 = HotelRoomReservation.objects.filter(hotel_room_id=validated_data['hotel_room'].id,
                                                     check_in__lte=check_in, check_out__gte=check_in).exists()

        case_2 = HotelRoomReservation.objects.filter(hotel_room_id=validated_data['hotel_room'].id,
                                                     check_in__lte=check_out, check_out__gte=check_out).exists()

        case_3 = HotelRoomReservation.objects.filter(hotel_room_id=validated_data['hotel_room'].id,
                                                     check_in__gte=check_in, check_out__lte=check_out).exists()

        if case_1 or case_2 or case_3:
            raise ObjectDoesNotExist('No such room available for this time duration!')
        else:
            return super(HotelRoomReservationSerializer, self).create(validated_data)


class VillaReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VillaReservation
        fields = ('user', 'check_in', 'check_out', 'villa')

    def create(self, validated_data):
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']

        case_1 = VillaReservation.objects.filter(villa=validated_data['villa'].id,
                                                 check_in__lte=check_in, check_out__gte=check_in).exists()

        case_2 = VillaReservation.objects.filter(villa=validated_data['villa'].id,
                                                 check_in__lte=check_out, check_out__gte=check_out).exists()

        case_3 = VillaReservation.objects.filter(villa=validated_data['villa'].id,
                                                 check_in__gte=check_in, check_out__lte=check_out).exists()

        if case_1 or case_2 or case_3:
            raise ObjectDoesNotExist('No such room available for this time duration!')
        else:
            return super(VillaReservationSerializer, self).create(validated_data)
