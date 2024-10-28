from django.db import models

# Create your models here.

class Veiculo(models.Model):
    veiculo = models.CharField(max_length=250)
    placa = models.CharField(max_length=15)
    marca = models.CharField(max_length=250)
    modelo = models.CharField(max_length=250)
    ano = models.CharField(max_length=250)
    cor = models.CharField(max_length=250)
    valor = models.CharField(max_length=250)
