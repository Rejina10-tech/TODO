from rest_framework import viewsets
from todoapp.models.todo import Todo
from todoapp.serializers.todo import ToDoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
