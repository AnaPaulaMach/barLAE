# Generated by Django 4.2.13 on 2024-07-10 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0025_item_cantidad_item_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='item',
            name='comentario',
        ),
    ]
