from django.urls import path
from .views import (
    RulesListAPIView,
)

urlpatterns = [
    path('rules-list/', RulesListAPIView.as_view(), name='rules-list'),
]
