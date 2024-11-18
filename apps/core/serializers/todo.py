from rest_framework import serializers
from apps.core.models.todo import Todo
from django.contrib.auth.models import User


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'