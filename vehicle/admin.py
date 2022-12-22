from django.contrib import admin
from vehicle.models import *


class AdminAirplane(admin.ModelAdmin):
    list_display = ('id', 'gate', 'title', 'is_valid', )
    search_fields = ('gate', 'is_valid', )


admin.site.register(Airplane, AdminAirplane)
