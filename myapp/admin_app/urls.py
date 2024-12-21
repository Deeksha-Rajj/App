from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet

router = DefaultRouter()
router.register(r'apps', AppViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]