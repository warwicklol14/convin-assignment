from django.urls import path,include
from rest_framework.routers import DefaultRouter
from taskreminder.api import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'task_trackers', views.TaskTrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]