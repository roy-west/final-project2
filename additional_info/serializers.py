from rest_framework import serializers
from .models import Address, Advantage, Question


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
        
class AdvantageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'
        
        
class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'