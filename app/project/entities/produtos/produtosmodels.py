from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    ingredientes = models.CharField(max_length=250)
    categoria = models.CharField(max_length=250)
    preco = models.FloatField()