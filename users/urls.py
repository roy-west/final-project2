from django.contrib import admin
from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('auth/', ObtainAuthToken.as_view()),
]