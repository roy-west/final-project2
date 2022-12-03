from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import datetime

from users.models import CustomUser
from .models import Computer, Order



@api_view(['GET', 'POST'])
def order_create(requests):
    user = CustomUser.objects.get(id=1)
    comp = Computer.objects.get(id=1)
    order = Order.objects.create(
        user=user,
        computer=comp,
        booking_time=datetime.now(),
    )
    return Response({'order_id': order.id})

