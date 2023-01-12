from typing import Tuple

from django.db import models

from discretions.models import AbstractComment, AbstractRate


class AbstractVehicle(models.Model):
    INTERNATIONAL = 50
    LOCAL = 51
    CATEGORY_CHOICES = (
        (INTERNATIONAL, 'International'),
        (LOCAL, 'Local')
    )

    title = models.CharField(max_length=100)
    origin = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    company = models.CharField(max_length=100)
    arrive_time = models.DateTimeField()
    depart_time = models.DateTimeField()
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=51)
    capacity = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Flight(AbstractVehicle):
    ECONOMY_CLASS = 1
    PREMIUM_ECONOMY_CLASS = 2
    BUSINESS_CLASS = 3
    FIRST_CLASS = 4

    FLIGHT_TYPE_CHOICES = (
        (ECONOMY_CLASS, "economy_class"),
        (PREMIUM_ECONOMY_CLASS, "Premium_economy_class"),
        (BUSINESS_CLASS, "Business_class"),
        (FIRST_CLASS, "First_class")
    )

    AIRBUS = 5
    BOEING = 6
    FOKKER = 7
    MCDONNELL_DOUGLAS = 8

    AIRPLANE_TYPE_CHIOCES = (
        (AIRBUS, "Airbus"),
        (BOEING, "Boeing "),
        (FOKKER, "Fokker"),
        (MCDONNELL_DOUGLAS, "McDonnell Douglas")
    )

    flight_type = models.PositiveSmallIntegerField(choices=FLIGHT_TYPE_CHOICES, default=1)
    is_valid = models.BooleanField(default=True)
    airplane_type = models.PositiveSmallIntegerField(choices=AIRPLANE_TYPE_CHIOCES, default=5)
    price = models.ForeignKey("FlightPrice", on_delete=models.CASCADE, related_name='flight_price')


class FlightPrice(models.Model):
    price = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class FlightComment(AbstractComment):
    hotel = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_comments')


class FlightRate(AbstractRate):
    hotel = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_rates')