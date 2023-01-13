from rest_framework import serializers
from payment.models import *


class HotelRoomPaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomPaymentHistory
        fields = ('id', 'user', 'reservation_obj', 'date', 'is_valid', )


class VillaPaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaPaymentHistory
        fields = ('id', 'user', 'reservation_obj', 'date', 'is_valid',)


