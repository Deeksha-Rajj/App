from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import App
from .serializers import AppSerializer
from rest_framework.permissions import IsAdminUser

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAdminUser]
