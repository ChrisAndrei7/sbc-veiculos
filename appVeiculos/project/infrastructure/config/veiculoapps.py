from django.apps import AppConfig
from entities import veiculos

class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'veiculos'
