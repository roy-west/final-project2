from rest_framework.generics import ListAPIView

from .models import Address, Advantage, Question
from .serializers import AddressListSerializer, AdvantageListSerializer, QuestionListSerializer


class AdvantageListAPIView(ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageListSerializer
    

class AddressListAPIView(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    
    
class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

