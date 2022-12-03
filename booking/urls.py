from django.urls import path
from .views import (
    OrderCreateAPIView,
    ComputerRoomListAPIView,
    ComputerListAPIView,
)

urlpatterns = [
    path('order-create/', OrderCreateAPIView.as_view(), name='order-create'),

    path('computer-room-list/', ComputerRoomListAPIView.as_view(),
         name='computer-room-list'),
    path('computer-list/', ComputerListAPIView.as_view(), name='computer-list'),
]
