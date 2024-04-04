from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from hotel_rooms.rooms.api.services import RoomService

def rooms_grpc_handlers(server):
    app_registry = AppHandlerRegistry("rooms", server)
    app_registry.register(RoomService)