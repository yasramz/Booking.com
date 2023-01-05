from django.contrib import admin
from payment.models import VillaPaymentHistory, HotelRoomPaymentHistory

admin.site.register(HotelRoomPaymentHistory)
admin.site.register(VillaPaymentHistory)

