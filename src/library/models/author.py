from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    first_name: str = models.CharField(
        max_length=100
    )
    last_name:str = models.CharField(
        max_length=100
    )
    birth_date: datetime = models.DateField(
        null=True,
        blank=True
    )
    profile = models.URLField(
        max_length=80,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    rating = models.FloatField(
        validators= [
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ],
        default=0
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}."