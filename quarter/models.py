from django.db import models


class Location(models.Model):
    address = models.TextField()
    map_link = models.TextField()


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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Mete:
        abstract = True

    def __str__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # available = models.IntegerField()
    avatar = None


class GeneralAvatar(models.Model):
    avatar = models.ImageField(upload_to='quarter/hotel/avatar')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class DetailAvatar(models.Model):
    avatar = models.ImageField(upload_to='quarter/quarter/avatar')
    quarter = models.ForeignKey(AbstractQuarter, on_delete=models.CASCADE)


class Villa(AbstractQuarter):
    AVAILABLE = 1
    FULL = 2
    AVAILABLENESS_CHOICES = (
        (AVAILABLE, 'Available'),
        (FULL, 'Full')
    )

    Available = models.PositiveSmallIntegerField(choices=AVAILABLENESS_CHOICES, default=AVAILABLE)


class HotelRoom(AbstractQuarter):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # availableness = None
