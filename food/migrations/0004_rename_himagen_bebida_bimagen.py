# Generated by Django 4.2.13 on 2024-06-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_bebida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bebida',
            old_name='hImagen',
            new_name='bImagen',
        ),
    ]
