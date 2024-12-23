# Generated by Django 4.2.13 on 2024-06-17 00:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_pedido_mesa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('finalizado', 'Finalizado')], default='activo', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mesa',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]
