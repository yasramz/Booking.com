from django.contrib import admin
from quarter.models import *
from django.contrib.admin.options import TabularInline


class AdminLocation(admin.ModelAdmin):
    list_display = ('address', 'is_valid',)
    search_fields = ('address', 'is_valid')


class AdminHotelAvatar(admin.ModelAdmin):
    list_display = ('avatar', )
    search_fields = ('is_valid',)


class AdminHotelRoomAvatar(admin.ModelAdmin):
    list_display = ('avatar',  'is_valid',)
    search_fields = ('is_valid',)


class AdminVillaAvatar(admin.ModelAdmin):
    list_display = ('avatar',  'is_valid',)
    search_fields = ('is_valid',)


class AdminVilla(admin.ModelAdmin):
    list_display = ('title', 'is_valid', )
    search_fields = ('title', 'is_valid', )


class AdminHotel(admin.ModelAdmin):
    list_display = ('title', 'is_valid', )
    search_fields = ('title', 'is_valid', )


class AdminHotelRoom(admin.ModelAdmin):
    list_display = ('title', 'is_valid',)
    search_fields = ('title', 'is_valid',)


admin.site.register(Location, AdminLocation)
admin.site.register(HotelAvatar, AdminHotelAvatar)
admin.site.register(HotelRoomAvatar, AdminHotelRoomAvatar)
admin.site.register(VillaAvatar, AdminVillaAvatar)
admin.site.register(Villa, AdminVilla)
admin.site.register(Hotel, AdminHotel)
admin.site.register(HotelRoom, AdminHotelRoom)
admin.site.register(HotelRoomPrice)
admin.site.register(VillaPrice)

