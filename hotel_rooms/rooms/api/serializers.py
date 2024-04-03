from django_socio_grpc import proto_serializers

from hotel_rooms.rooms.models import Room
from ..grpc.rooms_pb2 import (
    RoomResponse,
    RoomListResponse,
)


class RoomProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Room
        fields = ("id", "available", "n_of_beds", "numeration", "n_of_bathrooms")
        proto_class = RoomResponse
        proto_class_list = RoomListResponse
