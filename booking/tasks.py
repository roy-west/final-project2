from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from computer_club.celery import celery_app

from .models import Computer, Order


@celery_app.task(name='manage_computer')
def manage_computer(order_id):
    order = Order.objects.get(id=order_id)
    for computer in order.computers.all():
        computer.is_busy = True
        computer.save(update_fields=['is_busy'])

