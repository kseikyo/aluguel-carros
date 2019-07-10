from django.db import models
from cliente.models import CustomCliente
from carro.models import Carro
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 
# Create your models here.

def return_date_time():
    now = timezone.now
    return now

class AluguelManager(models.Manager):
    def create(self, carro, cliente, formas_de_pagamento, dias_de_aluguel, total,data_inicio):
        aluguel  = self.create(carro=carro, cliente=cliente, formas_de_pagamento=formas_de_pagamento, dias_de_aluguel=dias_de_aluguel, total=total, data_inicio=data_inicio)
        return aluguel

class Aluguel(models.Model):
    PAGAMENTOS = (
        ('Cartão de cŕedito', (
                ('Visa cŕedito', 'Visa cŕedito'),
                ('Mastercard crédito', 'Mastercard crédito')
            )
        ),
        ('Cartão de débito', (
                ('Visa débito', 'Visa débito'),
                ('Mastercard débito', 'Mastercard débito')
            )
        ),
        ('Dinheiro', (
                ('Real', 'Real'),
                ('Euro', 'Euro')
            )
        ),
        ('PicPay', (
                ('Saldo+Cartão', 'Saldo+Cartão'),
                ('Cartão de crédito', 'Cartão de crédito')
            )
        ),
        ('Criptomoedas', (
                ('Bitcoin', 'Bitcoin'),
                ('Trump coin', 'Trump coin')
            )
        ),
    )
    carro               = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente             = models.ForeignKey(CustomCliente, on_delete=models.CASCADE)
    formas_de_pagamento = models.CharField(max_length=100, choices=PAGAMENTOS)
    dias_de_aluguel     = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    total               = models.DecimalField(max_digits=10,blank=True, null=True, decimal_places=2)
    data_inicio         = models.DateTimeField(default=datetime.now, blank=True, editable=True)