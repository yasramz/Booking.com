from django.db import models


class AbstractVehicle:
    TIME_CHOICES = (
        (1, '00:00'), (2, '00:30'), (3, '01:00'), (4, '01:30'),
        (5, '02:00'), (6, '02:30'), (7, '03:00'), (8, '03:30'),
        (9, '04:00'), (10, '04:30'), (11, '05:00'), (12, '05:30'),
        (13, '06:00'), (14, '06:30'), (15, '07:00'), (16, '07:30'),
        (17, '08:00'), (18, '08:30'), (20, '09:00'), (21, '09:30'),
        (22, '10:00'), (23, '10:30'), (24, '11:00'), (25, '11:30'),
        (26, '12:00'), (27, '12:30'), (28, '13:00'), (29, '13:30'),
        (30, '14:00'), (31, '14:30'), (32, '15:00'), (33, '15:30'),
        (34, '16:00'), (35, '16:30'), (36, '17:00'), (37, '17:30'),
        (38, '18:00'), (39, '18:30'), (40, '19:00'), (41, '19:30'),
        (42, '20:00'), (43, '20:30'), (44, '21:00'), (45, '21:30'),
        (46, '22:00'), (47, '22:30'), (48, '23:00'), (49, '23:30'),
    )

    INTERNATIONAL = 50
    LOCAL = 51
    CATEGORY_CHOICES = (
        (INTERNATIONAL, 'International'),
        (LOCAL, 'Local')
    )

    title = models.CharField(max_length=100)
    origin = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    price = models.IntegerField()
    company = models.CharField(max_length=100)
    time = models.PositiveSmallIntegerField(choices=TIME_CHOICES, default=1)
    arrive_time = models.TimeField()
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=51)

    class Mete:
        abstract = True

