from django.apps import AppConfig


class TaskreminderConfig(AppConfig):
    name = 'taskreminder'

    def ready(self):
        # everytime server restarts
        import taskreminder.signals