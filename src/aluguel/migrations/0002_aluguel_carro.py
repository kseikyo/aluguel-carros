# Generated by Django 2.2.3 on 2019-07-06 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluguel', '0001_initial'),
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carro.Carro'),
        ),
    ]
