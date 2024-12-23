# Generated by Django 4.2.13 on 2024-06-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_hamburguesa_precio1_alter_hamburguesa_precio2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('precioC', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precioG', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hImagen', models.URLField()),
            ],
        ),
    ]
