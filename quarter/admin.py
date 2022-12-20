from django.contrib import admin
from quarter.models import *
from django.contrib.admin.options import TabularInline


class AdminLocation(admin.ModelAdmin):
    list_display = ('address', )
    search_fields = ('address',)


class AdminGeneralAvatar(admin.ModelAdmin):
    list_display = ('avatar', )


class AdminDetailAvatar(admin.ModelAdmin):
    list_display = ('avatar', )


class AdminVilla(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


class AdminHotel(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


class AdminHotelRoom(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


admin.site.register(Location, AdminLocation)
admin.site.register(GeneralAvatar, AdminGeneralAvatar)
admin.site.register(DetailAvatar, AdminDetailAvatar)
admin.site.register(Villa, AdminVilla)
admin.site.register(Hotel, AdminHotel)
admin.site.register(HotelRoom, AdminHotelRoom)

