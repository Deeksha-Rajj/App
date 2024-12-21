from django.db import models

# Create your models here.
# user_app/models.py
from django.contrib.auth.models import User
from admin_app.models import App  # Ensure this import is correct

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_tasks = models.ManyToManyField('Task', blank=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="tasks")
    app = models.ForeignKey(App, on_delete=models.CASCADE)  # ForeignKey to the App model
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.user_profile.user.username} on {self.app.name}"
