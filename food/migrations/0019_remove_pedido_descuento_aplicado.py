# Generated by Django 4.2.13 on 2024-06-18 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_pedido_descuento_aplicado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='descuento_aplicado',
        ),
    ]
