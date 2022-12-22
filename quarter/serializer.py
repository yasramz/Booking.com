from rest_framework import serializers
from .models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'map_link', 'is_valid',)


class GeneralAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralAvatar
        fields = ('avatar', 'is_valid',)


class DetailAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralAvatar
        fields = ('avatar', 'is_valid',)


class VillaSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    avatar = DetailAvatarSerializer(many=True)

    class Meta:
        model = Villa
        fields = ('title', 'description', 'capacity', 'price', 'facility', 'location', 'avatar',
                  'is_valid',)


class HotelSerializer(serializers.ModelSerializer):
    avatar = GeneralAvatarSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('title', 'description', 'is_valid', 'avatar')


class HotelRoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    location = LocationSerializer()
    avatar = DetailAvatarSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'capacity', 'price', 'facility', 'location', 'avatar',
                  'hotel', 'is_valid',)
