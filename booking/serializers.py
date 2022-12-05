from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .tasks import manage_computer
from .models import ComputerRoom, Computer, Order, RateComputerRoom


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'computers',
            'booking_time',
        ]

    def validate(self, attrs):
        computers = attrs['computers']
        booking_time = attrs['booking_time']
        print(attrs)
        if booking_time < timezone.now():
            raise ValidationError(
                {
                    'booking_time': 'Время не может в быть в прошлом'
                }
            )

        busy_computers = []
        orders = Order.objects.filter(
            computers__in=computers,
            booking_time__range=[booking_time - timezone.timedelta(minutes=15), booking_time]
        )
        for order in orders:
            for computer in order.computers.all():
                if computer.number not in busy_computers:
                    busy_computers.append(computer.number)

        if orders:
            raise ValidationError(
                {
                    'computers': f'В {booking_time} данные компьютеры заняты: {", ".join(busy_computers)}'
                }
            )
        return attrs

    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        validated_data = {**self.validated_data, **kwargs}
        print(validated_data)
        self.instance = self.create(validated_data)
        manage_computer.apply_async(
            (self.instance.id, ),
            eta=self.instance.booking_time,
        )
        return self.instance


class ComputerRoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerRoom
        fields = '__all__'


class ComputerListSerializer(serializers.ModelSerializer):
    booking_time = serializers.SerializerMethodField()

    def get_booking_time(self, obj):
        orders = Order.objects.filter(computers=obj)
        return [order.booking_time for order in orders]

    class Meta:
        model = Computer
        fields = '__all__'


class RateComputerRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateComputerRoom
        fields = '__all__'
