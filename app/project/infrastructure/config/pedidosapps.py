from django.apps import AppConfig
from entities import pedidos

class PedidoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedidos'
