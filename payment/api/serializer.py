from rest_framework import serializers
from payment.models import *


class HotelRoomPaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomPaymentHistory
        fields = ('user', 'reservation_obj', 'date', 'is_valid', )


class VillaPaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaPaymentHistory
        fields = ('user', 'reservation_obj', 'date', 'is_valid',)


