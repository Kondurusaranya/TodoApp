from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Task
        fields = "__all__"

    def get_queryset(self):
        return self.request.user.user_tasks

    def get_serializer_context(self):
        return {'request': self.request, }

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"], url_path='search/(?P<term>[^/.]+)')
    def search(self, request, term, *args, **kwargs):
        tasks = self.get_queryset().filter(Q(name__icontains=term) |
                                           Q(description__icontains=term) |
                                           Q(user__username__icontains=term))

        return Response({
            "data": self.serializer_class(tasks, many=True).data
        })
