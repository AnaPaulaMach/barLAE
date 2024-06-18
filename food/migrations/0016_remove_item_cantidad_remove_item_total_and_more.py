# Generated by Django 4.2.13 on 2024-06-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_item_cantidad_item_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='item',
            name='total',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cuenta',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
