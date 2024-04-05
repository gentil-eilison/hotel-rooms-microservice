from django_socio_grpc import proto_serializers

from hotel_rooms.bookings.models import Booking


class BookingProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Booking
        fields = ("id", "from_date", "until_date", "price", "room", "payment_id", "user_id")
