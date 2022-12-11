from .models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Пароли не совпадают!'})
        if CustomUser.objects.filter(phone_number=attrs['phone_number']):
            raise serializers.ValidationError({'phone_number': 'Такой номер уже зарегистрирован!'})
        if CustomUser.objects.filter(username=attrs['username']):
            raise serializers.ValidationError({'username': 'Такое имя пользователя уже зарегистрировано!'})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            phone_number=validated_data.get('phone_number')
        )
        return user
