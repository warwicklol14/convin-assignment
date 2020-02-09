from celery import shared_task
from .models import TaskModel
from .utils import getFilter
import logging

logger = logging.getLogger('Task Reminder Log')

@shared_task
def email_task_reminder(*args):
    task_type,update_type,email,created_at = args
    date_filter = getFilter(created_at,update_type)
    queryset = TaskModel.objects.filter(task_type=task_type,**date_filter)
    for task in queryset:
        logger.info(f'Sending email to {email} about task type {task_type}')

#celery -A convin worker -l info --without-gossip --without-mingle --without-heartbeat 
#celery -A convin beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler 