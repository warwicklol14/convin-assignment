from django.db import models

# Create your models here.
TYPE_ONE = 1
TYPE_TWO = 2
TYPE_THREE = 3
TYPE_FOUR = 4
TYPE_CHOICES = (
    (TYPE_ONE, 'Type one'),
    (TYPE_TWO, 'Type two'),
    (TYPE_THREE, 'Type three'),
    (TYPE_FOUR, 'Type four'),
)

class TaskModel(models.Model):
    task_type = models.IntegerField(verbose_name="Task type",choices=TYPE_CHOICES)
    task_desc = models.CharField(verbose_name="Task description",max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

class TaskTrackerModel(models.Model):
    UPDATE_DAILY = "DAILY"
    UPDATE_WEEKLY = "WEEKLY"
    UPDATE_MONTHLY = "MONTHLY"
    UPDATE_CHOICES = (
        (UPDATE_DAILY, 'Daily'),
        (UPDATE_WEEKLY, 'Weekly'),
        (UPDATE_MONTHLY, 'Monthly'),
    )
    task_type = models.IntegerField(verbose_name="Task type",choices=TYPE_CHOICES)
    update_type = models.CharField(verbose_name="Task update type",choices=UPDATE_CHOICES,max_length=15)
    email = models.CharField(verbose_name="Email address",max_length=40,unique=True)

    class Meta:
        verbose_name = "Task Tracker"
        verbose_name_plural = "Task Trackers"
