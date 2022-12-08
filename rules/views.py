from rest_framework.generics import ListAPIView

from .models import Rules
from .serializers import RulesListSerializer


class RulesListAPIView(ListAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesListSerializer

