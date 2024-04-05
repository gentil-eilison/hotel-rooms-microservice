from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from hotel_rooms.bookings.api.services import BookingService


def bookings_grpc_handlers(server):
    app_registry = AppHandlerRegistry("bookings", server)
    app_registry.register(BookingService)
