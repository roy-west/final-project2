from django.urls import path
from .views import (
    AddressListAPIView,
    AdvantageListAPIView,
    QuestionListAPIView,
)

urlpatterns = [
    path('address-list/', AddressListAPIView.as_view(), name='address-list'),
    path('advantage-list/', AdvantageListAPIView.as_view(), name='advantage-list'),
    path('question-list/', QuestionListAPIView.as_view(), name='question-list'),
]
