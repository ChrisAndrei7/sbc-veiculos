from django.apps import AppConfig
from entities import produtos

class ProdutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'
