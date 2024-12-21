from django.contrib import admin

# Register your models here.
# admin_app/admin.py

from django.contrib import admin
from .models import App

admin.site.register(App)

