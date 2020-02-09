from django.dispatch import receiver
from django.db import models
from .models import TaskTrackerModel
from .utils import getSchedule
from datetime import datetime
from django_celery_beat.models import PeriodicTask
import json

@receiver(models.signals.pre_save, sender=TaskTrackerModel)
def conversation_model_pre_save(sender, instance, **kwargs):
    schedule = getSchedule(instance.update_type)
    PeriodicTask.objects.create(
        crontab=schedule,                 
        name=f'Task Type {instance.task_type} Reminder {instance.update_type} for email address {instance.email}',    
        task='taskreminder.tasks.email_task_reminder',  
        args=json.dumps([instance.task_type,instance.update_type,instance.email,f'{datetime.now()}']),
    )