from django.apps import AppConfig
from entities import pagamentos

class PagamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagamentos'
