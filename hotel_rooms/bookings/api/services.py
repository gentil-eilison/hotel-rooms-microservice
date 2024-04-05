from django_socio_grpc import generics

from hotel_rooms.bookings.models import Booking
from .serializers import BookingProtoSerializer


class BookingService(generics.ModelService):
    queryset = Booking.objects.all()
    serializer_class = BookingProtoSerializer
