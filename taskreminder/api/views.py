from rest_framework import viewsets
from rest_framework import mixins,generics

from taskreminder.models import TaskModel,TaskTrackerModel
from taskreminder.api.serializers import TaskSerializer,TaskTrackerSerializer


class TaskViewSet(generics.ListCreateAPIView,
                generics.RetrieveUpdateAPIView,
                viewsets.GenericViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

class TaskTrackerViewSet(generics.CreateAPIView,
                        generics.ListCreateAPIView,
                        viewsets.GenericViewSet):
    queryset = TaskTrackerModel.objects.all()
    serializer_class = TaskTrackerSerializer