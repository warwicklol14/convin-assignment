from django_celery_beat.models import CrontabSchedule,IntervalSchedule
from datetime import datetime,date

def getCronTabSchedule(minute:str,hour:str,day_of_week:str,day_of_month:str,month_of_year:str):
    schedule,_ = CrontabSchedule.objects.get_or_create(minute=minute,hour=hour,day_of_week=day_of_week
                ,day_of_month=day_of_month,month_of_year=month_of_year)
    return schedule

def getDailySchedule():
    return getCronTabSchedule('0','5','*','*','*')

def getWeeklySchedule():
    return getCronTabSchedule('0','5','1','*','*')

def getMonthlySchedule():
    return getCronTabSchedule('0','5','*','1','*')

def getSchedule(update_type:str):
    if update_type == 'DAILY':
        return getDailySchedule()
    elif update_type == 'WEEKLY':
        return getWeeklySchedule()
    elif update_type == 'MONTHLY':
        return getMonthlySchedule()

def getTestSchedule():
    schedule, created = IntervalSchedule.objects.get_or_create(
     every=10,
     period=IntervalSchedule.SECONDS,
    )
    return schedule

def getFilter(created_at:str,update_type:str):
    created_date:datetime = datetime.fromisoformat(created_at)
    if update_type == 'MONTHLY':
        return {'created_at__year':created_date.year,'created_at__month':created_date.month}
    elif update_type == 'WEEKLY':
        return {'created_at__year':created_date.year,'created_at__week':created_date.isocalendar()[1]}
    elif update_type == 'DAILY':
        return {'created_at__year':created_date.year,'created_at__month':created_date.month,'created_at__day':created_date.day}