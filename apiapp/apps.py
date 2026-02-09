from django.apps import AppConfig


class ApiappConfig(AppConfig):
    name = 'apiapp'

    def ready(self):
        import apiapp.signals