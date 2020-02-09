from rest_framework import serializers
from taskreminder.models import TaskModel,TaskTrackerModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id','task_type', 'task_desc']


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTrackerModel
        fields = ['id','task_type', 'update_type','email']