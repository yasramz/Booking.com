from rest_framework import serializers, exceptions
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

    def create(self, validated_data):
        location = validated_data.pop('location', None)
        avatar = validated_data.pop('avatar', None)

        try:
            location = Location.objects.create(**location)
            VillaAvatar.objects.create(**avatar)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        villa = Villa.objects.create(location=location, **validated_data)

        return villa


class HotelSerializer(serializers.ModelSerializer):
    hotel_avatars = HotelAvatarSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('title', 'description', 'is_valid', 'hotel_avatars')

    def create(self, validated_data):
        hotel_avatars = validated_data.pop('hotel_avatars', None)
        try:
            hotel_avatars = Hotel.objects.create(**hotel_avatars)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        hotel = Villa.objects.create(hotel_avatars=hotel_avatars, **validated_data)

        return hotel


class HotelRoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    location = LocationSerializer()
    room_avatars = HotelRoomAvatarSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'capacity', 'price', 'facility', 'location', 'room_avatars',
                  'hotel', 'is_valid',)

    def create(self, validated_data):
        hotel = validated_data.pop('hotel', None)
        location = validated_data.pop('location', None)
        room_avatars = validated_data.pop('room_avatars', None)
        try:
            hotel = Hotel.objects.create(**hotel)
            location = Hotel.objects.create(**location)
            room_avatars = Hotel.objects.create(**room_avatars)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        hotel_room = HotelRoom.objects.create(hotel=hotel, location=location, room_avatars=room_avatars, **validated_data)

        return hotel_room

