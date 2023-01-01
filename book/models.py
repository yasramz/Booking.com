from django.db import models
from user.models import User
from vehicle.models import Flight
from quarter.models import Villa, HotelRoom


class AbstractVehicleReservation(models.Model):
    CANCELED = 1
    RESERVED = 2
    RESERVATION_CHOICES = (
        (CANCELED, 'Canceled'),
        (RESERVED, 'Reserved')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_reservations')
    reservation_time = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=RESERVATION_CHOICES, default=RESERVED)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FlightReservation(AbstractVehicleReservation):
    airplane = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='airplane_reservations')
    is_valid = models.BooleanField(default=True)


class AbstractQuarterReservation(models.Model):
    CANCELED = 1
    RESERVED = 2
    RESERVATION_CHOICES = (
        (CANCELED, 'Canceled'),
        (RESERVED, 'Reserved')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quarter_reservations')
    reservation_time = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=RESERVATION_CHOICES, default=RESERVED)
    check_In = models.DateTimeField()
    check_Out = models.DateTimeField()
    duration = models.DurationField()
    total_payment = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class HotelReservation(AbstractQuarterReservation):
    hotel = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_reservations')
    is_valid = models.BooleanField(default=True)


class VillaReservation(AbstractQuarterReservation):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='villa_reservations')
    is_valid = models.BooleanField(default=True)

