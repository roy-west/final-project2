from rest_framework.generics import ListAPIView

from .models import Food
from .serializers import FoodListSerializer


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer
