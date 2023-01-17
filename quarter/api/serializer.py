from rest_framework import serializers, exceptions

from payment.models import Currency
from quarter.models import *


# ----------------------------------------------- Location Serializer --------------------------------------------------
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'address', 'map_link', 'is_valid',)


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------- Price Serializers ----------------------------------------------------
class HotelRoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomPrice
        fields = ('id', 'price', 'is_valid',)


class VillaPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaPrice
        fields = ('id', 'price', 'is_valid',)


# ----------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------- Avatar Serializers ----------------------------------------------------
class HotelAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAvatar
        fields = ('id', 'avatar', 'is_valid',)


class HotelRoomAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomAvatar
        fields = ('id', 'avatar', 'is_valid',)


class VillaAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaAvatar
        fields = ('id', 'avatar', 'is_valid',)


# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------- Main Quarter Serializers -------------------------------------------------
class HotelSerializer(serializers.ModelSerializer):
    hotel_avatars = HotelAvatarSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'is_valid', 'hotel_avatars')

    def create(self, validated_data):
        hotel_avatars = validated_data.pop('hotel_avatars', None)
        try:
            hotel_avatars = HotelAvatar.objects.create(**hotel_avatars)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        hotel = Hotel.objects.create(hotel_avatars=hotel_avatars, **validated_data)

        return hotel


class VillaSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    villa_avatars = VillaAvatarSerializer(many=True)
    price = VillaPriceSerializer()
    preferred_currency = serializers.CharField(max_length=3, required=False)

    class Meta:
        model = Villa
        fields = ('id', 'title', 'description', 'capacity', 'price',
                  'facility', 'location', 'villa_avatars', 'is_valid', 'preferred_currency')

    def create(self, validated_data):
        location = validated_data.pop('location', None)
        villa_avatars = validated_data.pop('villa_avatars', None)

        try:
            location = Location.objects.create(**location)
            VillaAvatar.objects.create(**villa_avatars)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        villa = Villa.objects.create(location=location, **validated_data)

        return villa

    def to_representation(self, instance):
        representation = super(VillaSerializer, self).to_representation(instance)
        if representation['preferred_currency'] is not None:
            currency = Currency.objects.get(currency=representation['preferred_currency'])
            price = Villa.objects.get(id=representation['id']).price__price

            representation['price'] = price * currency.ratio

        return representation
    

class HotelRoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    location = LocationSerializer()
    room_avatars = HotelRoomAvatarSerializer(many=True)
    price = HotelRoomPriceSerializer()

    class Meta:
        model = HotelRoom
        fields = ('id', 'title', 'description', 'capacity', 'price', 'facility', 'location', 'room_avatars',
                  'hotel', 'is_valid', 'preferred_currency')

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

        hotel_room = HotelRoom.objects.create(hotel=hotel, location=location, room_avatars=room_avatars,
                                              **validated_data)

        return hotel_room

    def to_representation(self, instance):
        representation = super(HotelRoomSerializer, self).to_representation(instance)
        if self['preferred_currency']:
            currency = Currency.objects.get(currency=representation['preferred_currency'])
            price = HotelRoom.objects.get(id=representation['id']).price__price

            representation['price'] = price * currency.ratio

        return representation


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------- Comment & Rate Serializers -------------------------------------------------

# Comment:
class HotelCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelComment
        fields = ('id', 'parent', 'comment_body', 'status', 'hotel', 'user',)

    extra_kwarg = {
        'parent': {'required': False},
        'status': {'read_only': True},
    }


class HotelRoomCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomComment
        fields = ('id', 'parent', 'comment_body', 'status', 'hotel', 'user',)
        extra_kwarg = {
            'parent': {'required': False},
            'status': {'read_only': True},
        }


class VillaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaComment
        fields = ('id', 'parent', 'comment_body', 'status', 'hotel', 'user',)
        extra_kwarg = {
            'parent': {'required': False},
            'status': {'read_only': True},
        }


# Rate:
class HotelRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRate
        fields = ('id', 'hotel', 'user', 'rate',)


class HotelRoomRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomRate
        fields = ('id', 'hotel', 'user', 'rate',)


class VillaRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaRate
        fields = ('id', 'hotel', 'user', 'rate',)

# ----------------------------------------------------------------------------------------------------------------------
