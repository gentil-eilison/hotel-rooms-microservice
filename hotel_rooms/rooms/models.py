from django.db import models

# Create your models here.
class Room(models.Model):
    available = models.BooleanField(default=False, verbose_name="Available")
    n_of_beds = models.PositiveSmallIntegerField(verbose_name="Number of beds")
    numeration = models.PositiveSmallIntegerField(verbose_name="Room numeration")
    n_of_bathrooms = models.PositiveSmallIntegerField(verbose_name="Number of bathrooms")

    def __str__(self):
        return f"Room number {self.numeration}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"