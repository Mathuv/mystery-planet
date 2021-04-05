import uuid

from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class TimestampedModel(models.Model):
    """
    Abstract Model for timestamping create and updates.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(TimestampedModel, models.Model):
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)


class Person(TimestampedModel, models.Model):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = ((GENDER_MALE, "Male"), (GENDER_FEMALE, "Female"), (GENDER_OTHER, "Other"))

    EYE_BLUE = "blue"
    EYE_BROWN = "brown"
    EYE_COLOR_CHOICES = ((EYE_BLUE, "Blue"), (EYE_BROWN, "Brown"))

    index = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    has_died = models.BooleanField()
    picture = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    eye_color = models.CharField(max_length=20, choices=EYE_COLOR_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    greeting = models.TextField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    registered = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
