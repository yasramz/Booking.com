from django.db import models
from Booking import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class AbstractComment(models.Model):
    CREATED = 1
    APPROVED = 2
    REJECTED = 3
    DELETED = 4
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (DELETED, 'Deleted')
    )

    comment_body = models.TextField()

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=CREATED)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractRate(models.Model):
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
