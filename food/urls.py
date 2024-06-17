from django.urls import path

from . import views #el . quiere decir de esta carpeta

app_name = 'food' #food pq asi se llama nuestra app

urlpatterns = [
    path('hamburguesas/', views.hamburguesas, name="hamburguesas"),
    path('bebidas/', views.bebidas, name="bebidas"),
    path('pedido/', views.pedido, name="pedido"),
    path('exito/', views.exito, name="exito"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('', views.index, name='index'), #chequear
    path('descuentos/', views.descuentos, name='descuentos'),
    path('historial/', views.historial, name='historial'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('gestionar_descuentos/', views.gestionar_descuentos, name='gestionar_descuentos'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
    path('ver_solicitudes_modificacion/', views.ver_solicitudes_modificacion, name='ver_solicitudes_modificacion'),
    path('finalizar_pedido/<int:pedido_id>/', views.finalizar_pedido, name='finalizar_pedido'),
    path('desactivar_descuento/<int:descuento_id>/', views.desactivar_descuento, name='desactivar_descuento'),
    path('activar_descuento/<int:descuento_id>/', views.activar_descuento, name='activar_descuento'),
    path('eliminar_descuento/<int:descuento_id>/', views.eliminar_descuento, name='eliminar_descuento'),
]

