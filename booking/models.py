from django.db import models
from users.models import CustomUser


class ComputerRoom(models.Model):
    room_type = models.CharField(max_length=255)
    computers_quantity = models.IntegerField()
    description = models.TextField()


class Computer(models.Model):
    room = models.ForeignKey(ComputerRoom, on_delete=models.CASCADE, related_name='computers')
    number = models.CharField(max_length=255)
    additional_description = models.TextField(blank=True, null=True)
    is_busy = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='orders')
    booking_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)




