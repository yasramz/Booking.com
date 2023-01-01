from rest_framework import mixins, viewsets
from user.api.serializer import UserSerializer, BankInfoSerializer, ProfileSerializer
from user.models import User, Profile, BankInfo

