# user_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
     path('apps/', views.app_list, name='app_list'),  # API endpoint to get apps
]