from django.apps import AppConfig
from entities import pacientes

class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pacientes'
