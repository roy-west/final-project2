from .models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Jopa'})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password')
        )
        return user