from rest_framework import serializers
from quarter.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'map_link', 'is_valid',)


class HotelAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAvatar
        fields = ('avatar', 'is_valid',)


class HotelRoomAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomAvatar
        fields = ('avatar', 'is_valid',)


class VillaAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        class Meta:
            model = VillaAvatar
            fields = ('avatar', 'is_valid',)


class VillaSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    avatar = VillaAvatarSerializer(many=True)

    class Meta:
        model = Villa
        fields = ('title', 'description', 'capacity', 'price', 'facility', 'location', 'avatar',
                  'is_valid',)


class HotelSerializer(serializers.ModelSerializer):
    hotel_avatars = HotelAvatarSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('title', 'description', 'is_valid', 'hotel_avatars')


class HotelRoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    location = LocationSerializer()
    room_avatars = HotelRoomAvatarSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'capacity', 'price', 'facility', 'location', 'room_avatars',
                  'hotel', 'is_valid',)
