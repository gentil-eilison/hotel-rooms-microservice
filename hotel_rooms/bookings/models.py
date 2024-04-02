from django.db import models

from hotel_rooms.rooms.models import Room

# Create your models here.
class Booking(models.Model):
    from_date = models.DateTimeField(verbose_name="From")
    until_date = models.DateTimeField(verbose_name="Until")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Price")
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.PROTECT, verbose_name="Room")
    payment_id = models.PositiveBigIntegerField(verbose_name="Payment ID")
    user_id = models.PositiveBigIntegerField(verbose_name="User ID")

    def __str__(self):
        return f"Room {self.room.numeration} from {self.from_date.date} until {self.until_date.date}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
