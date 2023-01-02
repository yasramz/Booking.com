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
        fields = ('user', 'reservation_time', 'status', 'flight')

    def create(self, validated_data):
        flight = Flight.objects.get(id=self.get_value('flight'))

        if flight.capacity > 0:
            flight.capacity = flight.capacity - 1
            flight.save()
            super(FlightReservationSerializer, self).create(validated_data)
        else:
            raise ObjectDoesNotExist('No sit available')


class HotelRoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomReservation
        fields = ('user', 'reservation_time', 'status', 'check_In', 'check_Out', 'duration', 'total_payment', 'hotel_room')

    def create(self, validated_data):
        check_in = self.get_value('check_In')
        check_out = self.get_value('check_Out')

        case_1 = HotelRoomReservation.objects.filter(hotel_room_id=self.get_value('hotel_room'),
                                                     check_in__lte=check_in, check_out__gte=check_in).exists()

        case_2 = HotelRoomReservation.objects.filter(hotel_room_id=self.get_value('hotel_room'),
                                                     check_in__lte=check_out, check_out__gte=check_out).exists()

        case_3 = HotelRoomReservation.objects.filter(hotel_room_id=self.get_value('hotel_room'),
                                                     check_in__gte=check_in, check_out__lte=check_out).exists()

        if case_1 or case_2 or case_3:
            raise ObjectDoesNotExist('No such room available for this time duration!')
        else:
            super(HotelRoomReservationSerializer, self).create(validated_data)


class VillaReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VillaReservation
        fields = ('user', 'reservation_time', 'status', 'check_in', 'check_out', 'duration', 'total_payment', 'villa')

    def create(self, validated_data):
        check_in = self.get_value('check_in')
        check_out = self.get_value('check_out')

        case_1 = VillaReservation.objects.filter(villa=self.get_value('villa'),
                                                 check_in__lte=check_in, check_out__gte=check_in).exists()

        case_2 = VillaReservation.objects.filter(villa=self.get_value('villa'),
                                                 check_in__lte=check_out, check_out__gte=check_out).exists()

        case_3 = VillaReservation.objects.filter(villa=self.get_value('villa'),
                                                 check_in__gte=check_in, check_out__lte=check_out).exists()

        if case_1 or case_2 or case_3:
            raise ObjectDoesNotExist('No such room available for this time duration!')
        else:
            super(VillaReservationSerializer, self).create(validated_data)
