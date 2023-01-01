import math, random
from rest_framework_simplejwt.tokens import RefreshToken


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