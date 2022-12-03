from django.urls import path
from .views import (
    FoodListAPIView,
)

urlpatterns = [
    path('food-list/', FoodListAPIView.as_view(), name='food-list'),
]
