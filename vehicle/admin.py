from django.contrib import admin
from vehicle.models import *


class AdminAirplane(admin.ModelAdmin):
    list_display = ('id', 'gate', 'title', )
    search_fields = ('gate', )


admin.site.register(Airplane, AdminAirplane)
