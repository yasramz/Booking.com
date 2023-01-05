from django.db import models
from book.models import HotelRoomReservation, VillaReservation
from user.models import User


class HotelRoomPaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_payment')
    reservation_obj = models.ForeignKey(HotelRoomReservation, on_delete=models.DO_NOTHING, related_name='hotelroom_payment_history')
    is_valid = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class VillaPaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_villa_payment')
    reservation_obj = models.ForeignKey(VillaReservation, on_delete=models.DO_NOTHING, related_name='villa_payment_history')
    is_valid = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

