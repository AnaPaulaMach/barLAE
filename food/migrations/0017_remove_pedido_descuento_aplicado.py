# Generated by Django 4.2.13 on 2024-06-18 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0016_remove_item_cantidad_remove_item_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='descuento_aplicado',
        ),
    ]
