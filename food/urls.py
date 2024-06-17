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
]

