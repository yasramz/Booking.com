from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class User(AbstractUser):
    phone_number = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    password = models.CharField(max_length=120,
                                validators=[RegexValidator(regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                                           message="Minimum eight characters, at least one letter and "
                                                                   "one number")])
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    national_code = models.CharField(max_length=30)
    emergency_number = models.IntegerField()
    date_of_birth = models.DateTimeField()
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Bank_Info(models.Model):
    account_number = models.IntegerField()
    shaba_number = models.IntegerField()
    card_number = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
