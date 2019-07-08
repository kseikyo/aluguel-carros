from django.db import models

# Create your models here.
class Datas(models.Model):
    data_carro        = models.ForeignKey('carro.Carro', on_delete=models.CASCADE)
    datas_disponíveis = models.DateTimeField()