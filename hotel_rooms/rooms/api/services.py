from django_socio_grpc import generics

from hotel_rooms.rooms.models import Room
from .serializers import RoomProtoSerializer


class RoomService(generics.ModelService):
    queryset = Room.objects.all()
    serializer_class = RoomProtoSerializer
