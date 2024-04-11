from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Room(models.Model):
    available = models.BooleanField(default=True, verbose_name="Available")
    n_of_beds = models.PositiveSmallIntegerField(verbose_name="Number of beds", validators=[MinValueValidator(1)])
    numeration = models.PositiveSmallIntegerField(verbose_name="Room numeration", validators=[MinValueValidator(1)], unique=True)
    n_of_bathrooms = models.PositiveSmallIntegerField(verbose_name="Number of bathrooms", validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Room number {self.numeration}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"