from django.contrib import admin
from vehicle.models import *


class AdminAirplane(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', )
    search_fields = ('is_valid', )


admin.site.register(Flight)
admin.site.register(FlightPrice)
