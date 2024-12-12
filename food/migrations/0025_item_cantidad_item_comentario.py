# Generated by Django 4.2.13 on 2024-07-10 05:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0024_bebida_descripcion_hamburguesa_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cantidad',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='item',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
