# Generated by Django 4.2.13 on 2024-06-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_alter_pedido_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cuenta',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
