# Generated by Django 2.2.3 on 2019-07-06 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='alugado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        )
    ]