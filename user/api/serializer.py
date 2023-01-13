from abc import ABC

from rest_framework import serializers, exceptions
from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'USERNAME_FIELD', )


class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'account_number', 'shaba_number', 'card_number', )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # bank_info = BankInfoSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'national_code', 'emergency_number', 'date_of_birth', 'gender', 'user',) #'bank_info',

    def create(self, validated_data):
        user = validated_data.pop('user', None)
        bank_info = validated_data.pop('bank_info', None)

        try:
            user = User.objects.create(**user)
            bank_info = BankInfo.objects.create(**bank_info)

        except(ValueError, TypeError):
            raise exceptions.ValidationError('data in not valid')

        profile = Profile.objects.create(user=user, bank_info=bank_info, **validated_data)

        return profile


class StepOneLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()


class StepTwoLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

