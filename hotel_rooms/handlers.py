from hotel_rooms.rooms.handlers import rooms_grpc_handlers
from hotel_rooms.bookings.handlers import bookings_grpc_handlers

def grpc_handlers(server):
    rooms_grpc_handlers(server)
    bookings_grpc_handlers(server)
