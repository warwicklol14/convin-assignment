from django.contrib import admin
from .models import TaskModel,TaskTrackerModel

admin.site.register(TaskModel)
admin.site.register(TaskTrackerModel)
