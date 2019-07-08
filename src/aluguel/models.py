from django.db import models
from cliente.models import CustomCliente
from carro.models import Carro

# Create your models here.
class Aluguel(models.Model):
    PAGAMENTOS = (
        ("Cartão de cŕedito", (
                ('Visa cŕedito', 'visa cŕedito'),
                ('Mastercard crédito', 'mastercard crédito')
            )
        ),
        ("Cartão de débito", (
                ('Visa débito', 'visa débito'),
                ('Mastercard débito', 'mastercard débito')
            )
        ),
        ("Dinheiro", "Real"),
        ("PicPay", "Saldo+Cartão"),
        ("Bitcoin", "BTC"),
    )
    carro               = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente             = models.ForeignKey(CustomCliente, on_delete=models.CASCADE)
    formas_de_pagamento = models.CharField(max_length=100, choices=PAGAMENTOS)