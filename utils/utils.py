import math, random
from rest_framework_simplejwt.tokens import RefreshToken
from math import ceil
from quarter.models import AbstractPrice


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def generate_otp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]

    return otp


def change_price_for_all(num=None, model=None):
    for item in model.objects.all():
        multiplier = num / 100.
        old_price = item.price
        new_price = ceil(old_price + (old_price * multiplier))
        item.price = new_price
        item.save(update_fields=['price'])
