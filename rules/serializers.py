from rest_framework import serializers

from .models import Rules


class RulesListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Rules
        fields = '__all__'
