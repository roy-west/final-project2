from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import ComputerRoom, Computer, Order,  RateComputerRoom
from .serializers import (
    OrderCreateSerializer,
    ComputerRoomListSerializer,
    ComputerListSerializer,
    RateComputerRoomSerializer
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


class RateComputerRoomAPIView(ListAPIView):
    queryset = RateComputerRoom.objects.all()
    serializer_class = RateComputerRoomSerializer

