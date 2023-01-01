from abc import ABC

from rest_framework import serializers
from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password', 'USERNAME_FIELD', )


class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('account_number', 'shaba_number', 'card_number', )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    bank_info = BankInfoSerializer()

    class Meta:
        model = Profile
        fields = ('national_code', 'emergency_number', 'date_of_birth', 'gender', 'user', 'bank_info', )


class StepOneLoginSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])


class StepTwoLoginSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])
    code = serializers.CharField(max_length=6)

