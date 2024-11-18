from rest_framework import viewsets
from apps.core.models.todo import Todo
from apps.core.serializers.todo import ToDoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
