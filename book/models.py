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

    reservation_time = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=RESERVATION_CHOICES, default=RESERVED)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FlightReservation(AbstractVehicleReservation):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_reservations')
    airplane = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='airplane_reservations')
    is_valid = models.BooleanField(default=True)


class AbstractQuarterReservation(models.Model):
    CANCELED = 1
    RESERVED = 2
    APPROVED = 3
    RESERVATION_CHOICES = (
        (CANCELED, 'Canceled'),
        (RESERVED, 'Reserved'),
        (APPROVED, 'approved')
    )

    reservation_time = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=RESERVATION_CHOICES, default=RESERVED)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    duration = models.DurationField()
    total_payment = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class HotelRoomReservation(AbstractQuarterReservation):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotelroom_reservations')
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_reservations')
    is_valid = models.BooleanField(default=True)


class VillaReservation(AbstractQuarterReservation):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='villa_reservations')
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='villa_reservations')
    is_valid = models.BooleanField(default=True)
