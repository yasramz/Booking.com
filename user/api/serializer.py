from abc import ABC

from rest_framework import serializers, exceptions
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
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])


class StepTwoLoginSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])
    code = serializers.CharField(max_length=6)

