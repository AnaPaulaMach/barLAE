# Generated by Django 4.2.13 on 2024-06-10 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hamburguesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('precio1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('precio2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('hImagen', models.URLField()),
            ],
        ),
    ]
