from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Create your models here. 
# Un modelo es una clase de Python, sirve para ordenar.
# Django convierte los modelos en tablas para las BD

class Hamburguesa(models.Model):
    nombre  = models.CharField(max_length=120)
    precio1 = models.DecimalField(max_digits=10, decimal_places = 2) #2 precios 1 hamb grande otra chica
    precio2 = models.DecimalField(max_digits=10, decimal_places = 2)
    descripcion = models.CharField(max_length=500, default='')
    hImagen = models.URLField()


class Bebida(models.Model):
    nombre  = models.CharField(max_length=120)
    precioC = models.DecimalField(max_digits=8, decimal_places = 2) #2 precios 1 hamb grande otra chica
    precioG = models.DecimalField(max_digits=8, decimal_places = 2)
    descripcion = models.CharField(max_length=500, default='')
    bImagen = models.URLField() 
# Creamos migrations en la terminal
# Migrations permite convertir codigo de python en codigo sql
# python3 manage.py migrate para hacer cambios en la BD
# python3 manage.py shell usamos la consola de python para aniadir hambus


class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    mesa = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(30)])
    numero = models.CharField(max_length=90, unique=True)
    cuenta = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True, blank=True)
    note = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('finalizado', 'Finalizado')], default='activo')
    
    
    def __str__(self):
        return f"Pedido #{self.numero} - Mesa: {self.mesa} - Estado: {self.estado}"

    class Meta:
        ordering = ['-date'] #Se ordenaran por fecha

   
class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=90)

class Descuento(models.Model):
    nombre_descuento = models.CharField(max_length=100, default='')
    cantidad_minima = models.IntegerField(default=0)
    cantidad_maxima = models.IntegerField(default=0)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.porcentaje_descuento}% para pedidos entre {self.cantidad_minima} y {self.cantidad_maxima}"
