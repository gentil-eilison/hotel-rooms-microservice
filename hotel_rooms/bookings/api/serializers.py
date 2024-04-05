from django_socio_grpc import proto_serializers

from hotel_rooms.bookings.models import Booking
from ..grpc.bookings_pb2 import (
    BookingResponse,
    BookingListResponse,
)


class BookingProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Booking
        fields = ("id", "from_date", "until_date", "price", "room", "payment_id", "user_id")
        proto_class = BookingResponse
        proto_list_class = BookingListResponse
