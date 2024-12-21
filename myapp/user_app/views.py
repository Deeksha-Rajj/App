from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UserProfile, Task
from .serializers import UserProfileSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# user_app/views.py

from django.shortcuts import render

def upload_task(request):
    return render(request, 'upload_task.html')

# user_app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import App
from .serializers import AppSerializer

@api_view(['GET'])
def app_list(request):
    apps = App.objects.all()
    serializer = AppSerializer(apps, many=True)
    return Response(serializer.data)



