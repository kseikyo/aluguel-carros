# Generated by Django 2.2.3 on 2019-07-10 00:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_aluguel_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='dias_de_aluguel',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='formas_de_pagamento',
            field=models.CharField(choices=[('Cartão de cŕedito', (('Visa cŕedito', 'Visa cŕedito'), ('Mastercard crédito', 'Mastercard crédito'))), ('Cartão de débito', (('Visa débito', 'Visa débito'), ('Mastercard débito', 'Mastercard débito'))), ('Dinheiro', (('Real', 'Real'), ('Euro', 'Euro'))), ('PicPay', (('Saldo+Cartão', 'Saldo+Cartão'), ('Cartão de crédito', 'Cartão de crédito'))), ('Criptomoedas', (('Bitcoin', 'Bitcoin'), ('Trump coin', 'Trump coin')))], max_length=100),
        ),
    ]
