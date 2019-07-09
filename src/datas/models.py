from django.db import models

# Create your models here.
class Datas(models.Model):
    data_carro        = models.ForeignKey('carro.Carro', on_delete=models.CASCADE, null=True, blank=True)
    datas_disponíveis = models.DateField()


    def __str__(self):
        if(self.data_carro):
            return f'Data do carro {self.data_carro.nome}'
        return 'Data do carro None' 