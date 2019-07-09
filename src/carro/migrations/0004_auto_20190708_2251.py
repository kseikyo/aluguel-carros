# Generated by Django 2.2.3 on 2019-07-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0003_auto_20190708_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='datas_disponíveis',
            field=models.ManyToManyField(to='datas.Datas'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='preco',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
