from django.contrib import admin
from book.models import FlightReservation, HotelRoomReservation, VillaReservation

admin.site.register(FlightReservation)
admin.site.register(HotelRoomReservation)
admin.site.register(VillaReservation)
