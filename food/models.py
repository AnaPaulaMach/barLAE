from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
# Un modelo es una clase de Python, sirve para ordenar.
# Django convierte los modelos en tablas para las BD

class Hamburguesa(models.Model):
    nombre  = models.CharField(max_length=120)
    precio1 = models.DecimalField(max_digits=10, decimal_places = 2) #2 precios 1 hamb grande otra chica
    precio2 = models.DecimalField(max_digits=10, decimal_places = 2)
    hImagen = models.URLField()


class Bebida(models.Model):
    nombre  = models.CharField(max_length=120)
    precioC = models.DecimalField(max_digits=8, decimal_places = 2) #2 precios 1 hamb grande otra chica
    precioG = models.DecimalField(max_digits=8, decimal_places = 2)
    bImagen = models.URLField() 
# Creamos migrations en la terminal
# Migrations permite convertir codigo de python en codigo sql
# python3 manage.py migrate para hacer cambios en la BD
# python3 manage.py shell usamos la consola de python para aniadir hambus

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE) # Si eliminamos usuario eliminamos sus ordenes
    numero  = models.CharField(max_length=90)
    cuenta  = models.DecimalField(max_digits=12, decimal_places = 2)
    date    = models.DateTimeField(auto_now_add=True, blank=True)  # Dia creacion orden
    note    = models.TextField(blank=True, null=True)
    mesa    = models.IntegerField(default=0)


# No podemos aniadir todos los items a Pedido pq no sabemos la cantidad de item que
# va a pedir un cliente para ello se crea el modelo Item

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=10, decimal_places = 2)
    size   = models.CharField(max_length=90)