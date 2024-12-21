from django.db import models

# Create your models here.
# admin_app/models.py

# admin_app/models.py
from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return self.name

