from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from tasks.choices import Priority, Status


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} - {self.email}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.status}"
