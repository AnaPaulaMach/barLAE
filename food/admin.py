from django.contrib import admin

#Para modificarlos como admin debemos agregar los modelos aqui
from .models import Hamburguesa, Bebida, Pedido, Item, Descuento 

# Register your models here.

class HamburguesaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio1', 'precio2', 'hImagen') #lista de lo que queremos ver en la pag de admin

admin.site.register(Hamburguesa, HamburguesaAdmin)

class BebidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precioC', 'precioG', 'bImagen') #lista de lo que queremos ver en la pag de admin
    

admin.site.register(Bebida, BebidaAdmin) 

admin.site.register(Pedido) 


admin.site.register(Item)

class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_descuento', 'cantidad_minima', 'cantidad_maxima', 'porcentaje_descuento', 'activo') #lista de lo que queremos ver en la pag de descuento 
admin.site.register(Descuento, DescuentoAdmin)