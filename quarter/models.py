from django.db import models


class Location(models.Model):
    address = models.TextField()
    map_link = models.TextField()
    country = models.TextField()
    city = models.TextField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class AbstractQuarter(models.Model):
    DOCTOR_CARE = 1
    FREE_WIFI = 2
    MEDICAL_SOCIAL_SERVICE = 3
    FACILITY_CHOICES = (
        (DOCTOR_CARE, 'Doctor_Care'),
        (FREE_WIFI, 'Free_WIFI'),
        (MEDICAL_SOCIAL_SERVICE, 'Media_Social_Service')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    facility = models.PositiveSmallIntegerField(choices=FACILITY_CHOICES, default=FREE_WIFI)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='quarters')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Mete:
        abstract = True

    def __str__(self):
        return self.title


class Hotel(models.Model):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

    HOTEL_STARS_CHOICES = (
        (ONE_STAR, '1_star'),
        (TWO_STAR, '2_star'),
        (THREE_STAR, '3_star'),
        (FOUR_STAR, '4_star'),
        (FIVE_STAR, '5_star')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    hotel_star = models.PositiveSmallIntegerField(choices=HOTEL_STARS_CHOICES, default=5)
    # available = models.IntegerField()
    # avatar = None
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class HotelAvatar(models.Model):
    avatar = models.ImageField(upload_to='quarter/hotel/avatar')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_avatars')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Villa(AbstractQuarter):
    AVAILABLE = 1
    FULL = 2
    AVAILABLENESS_CHOICES = (
        (AVAILABLE, 'Available'),
        (FULL, 'Full')
    )

    Available = models.PositiveSmallIntegerField(choices=AVAILABLENESS_CHOICES, default=AVAILABLE)
    is_valid = models.BooleanField(default=True)


class VillaAvatar(models.Model):
    avatar = models.ImageField(upload_to='quarter/villa/avatar')
    quarter = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='villa_avatars')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class HotelRoom(AbstractQuarter):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # availableness = None
    is_valid = models.BooleanField(default=True)


class HotelRoomAvatar(models.Model):
    avatar = models.ImageField(upload_to='quarter/hotelroom/avatar')
    quarter = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_avatars')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)