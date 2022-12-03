from django.db import models
from users.models import CustomUser


class ComputerRoom(models.Model):
    room_type = models.CharField(max_length=255)
    computers_quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.room_type


class RateComputerRoom(models.Model):
    room = models.OneToOneField(ComputerRoom, on_delete=models.CASCADE,
                                related_name='rate')
    one_hour = models.DecimalField(max_digits=10, decimal_places=0,
                                   verbose_name='Цена (час)')
    three_hours = models.DecimalField(max_digits=10, decimal_places=0,
                                      verbose_name='Цена (3 часа)')
    five_hours = models.DecimalField(max_digits=10, decimal_places=0,
                                     verbose_name='Цена (5 часов)')
    seven_hours = models.DecimalField(max_digits=10, decimal_places=0,
                                      verbose_name='Цена (7 часов)')
    night = models.DecimalField(max_digits=10, decimal_places=0,
                                verbose_name='Цена (22:00 - 18:00)')

    def __str__(self):
        return self.room


class Computer(models.Model):
    room = models.ForeignKey(ComputerRoom, on_delete=models.CASCADE,
                             related_name='computers')
    number = models.CharField(max_length=255)
    additional_description = models.TextField(blank=True, null=True)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room} | {self.number}'


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='orders',
                             verbose_name='Пользователь')
    room = models.ForeignKey(ComputerRoom, on_delete=models.SET_NULL,
                             related_name='orders', blank=True, null=True,
                             verbose_name='Зал')
    computers = models.ManyToManyField(Computer,
                                       related_name='orders',
                                       verbose_name='Компьютеры')
    booking_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room} | {self.computers.count()} шт.'
