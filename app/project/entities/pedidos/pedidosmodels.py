from django.db import models

class Pedido(models.Model):
    valor = models.FloatField()
    quantidade = models.IntegerField()
    produto_id = models.IntegerField()
    cliente_id = models.IntegerField()
    descricao = models.CharField(max_length=250)
    status = models.CharField(max_length=25)
    #RECEBIDO, EM_PREPARACAO, PRONTO, FINALIZADO
