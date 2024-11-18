from rest_framework import serializers
from todoapp.models.todo import Todo
from django.contrib.auth.models import User


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'