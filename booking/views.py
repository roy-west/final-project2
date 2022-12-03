from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import ComputerRoom, Computer, Order
from .serializers import (
    OrderCreateSerializer,
    ComputerRoomListSerializer,
    ComputerListSerializer,
)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]


class ComputerRoomListAPIView(ListAPIView):
    queryset = ComputerRoom.objects.all()
    serializer_class = ComputerRoomListSerializer


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerListSerializer
