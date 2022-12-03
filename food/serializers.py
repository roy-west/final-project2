from rest_framework import serializers

from .models import Food


class FoodListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Food
        fields = '__all__'
