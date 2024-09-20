from django.db import models

# Create your models here.

class Medico(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=15)
    crm = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    senha = models.CharField(max_length=250)
