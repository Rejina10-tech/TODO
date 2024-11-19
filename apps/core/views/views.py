from rest_framework import viewsets
from apps.core.models.todo import Todo
from apps.core.serializers.todo import ToDoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)