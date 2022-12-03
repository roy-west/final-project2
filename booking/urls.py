from django.urls import path
from .views import order_create


urlpatterns = [
    path('order-create/', order_create),
]
