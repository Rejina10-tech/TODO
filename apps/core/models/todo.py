from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default= False, blank=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, related_name="tasks")

    def __str__(self):
        return self.title