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
