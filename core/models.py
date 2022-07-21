from django.db import models
from django.contrib.auth.models import User


class TaskStatusChoices(models.TextChoices):
    Completed = "Completed"
    Pending = "Pending"


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dead_line = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=TaskStatusChoices.choices,
                              default=TaskStatusChoices.Pending)
    user = models.ForeignKey(User, related_name="user_tasks", on_delete=models.CASCADE)
