from django.db import models

class Pagamento(models.Model):
    pedido_id = models.IntegerField()
    status = models.CharField(max_length=25)
    valor = models.FloatField()
