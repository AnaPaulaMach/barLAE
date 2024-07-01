from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Hamburguesa, Bebida, Pedido, Item, Descuento
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm, DescuentoForm
from django.contrib import messages
import random
import json
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User  # Importa el modelo de usuario correctamente


def randomOrderNumber(length): # El numero de orden sera random
    sample  = 'ABCDEFGH0123456789'
    numeroO =''.join((random.choice(sample) for i in range(length)))
    return numeroO 

# Create your views here. View es una funcion de python


# Vista de inicio para el usuario regular
def index(request):
    if request.user.is_staff:  # Verifica si el usuario es un administrador
        return admin_index(request)  # Redirige a la vista de inicio del administrador
    else:
        request.session.set_expiry(0)
        ctx = {'active_link': 'index'}
        return render(request, 'food/index.html', ctx)
#la funcion render tranfroma el codigo html a httpresponse

# Vista de inicio para el administrador
@staff_member_required
def admin_index(request):
    # Lógica para la vista de inicio del administrador
    return render(request, 'food/admin_index.html')


def hamburguesas(request):
    request.session.set_expiry(0)
    hamburguesas = Hamburguesa.objects.all()
    ctx = {'hamburguesas': hamburguesas, 'active_link':'hamburguesa'}
    return render(request, 'food/hamburguesas.html', ctx)


def bebidas(request):
    request.session.set_expiry(0)
    bebidas = Bebida.objects.all()
    ctx = {'bebidas': bebidas, 'active_link':'bebida'}
    return render(request, 'food/bebidas.html', ctx)



@csrf_exempt
def pedido(request):
    request.session.set_expiry(0)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # is_ajax ya no se usa
        request.session['note'] = request.POST.get('note')  # note es el comentario
        request.session['pedido'] = request.POST.get('pedidos')
        pedidos = json.loads(request.session['pedido'])
        request.session['cuenta'] = request.POST.get('cuenta')
        mesa = request.POST.get('mesa')  # Obtener el número de mesa

        randomNum = randomOrderNumber(6)
        while Pedido.objects.filter(numero=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            pedido = Pedido(
                cliente=request.user,
                numero=randomNum,
                cuenta=float(request.session['cuenta']),
                note=request.session['note'],
                mesa=mesa  # Guardar el número de mesa
            )
            pedido.save()
            request.session['pedidoNum'] = pedido.numero
            for articulo in pedidos:
                try:
                    precio_str = articulo[2].replace(',', '.')
                    precio = float(precio_str)
                    item = Item(
                        pedido=pedido,
                        nombre=articulo[0],
                        precio=precio,
                        size=articulo[1],
                    )
                    item.save()
                except ValueError as e:
                    print(f"Error al convertir el precio de '{articulo[2]}': {e}")

    mesas = list(range(1, 31))  # Lista de numeros de mesa
    ctx = {'active_link': 'pedido', 'mesas': mesas}
    return render(request, 'food/pedido.html', ctx)



#session para guardar info que son similares a local storage
# son diccionarios , tienen expire time
# 0 significa que van a expirar cuando se cierre el navegador


#Vista succes para cuando un cliente realice su orden
def exito(request):
    pedidoNum = request.session['pedidoNum']
    cuenta = request.session['cuenta'] 
    items = Item.objects.filter(pedido__numero = pedidoNum)
    pedido = get_object_or_404(Pedido, numero=pedidoNum)
    ctx = {'pedidoNum':pedidoNum, 'cuenta':cuenta, 'items':items,'pedido': pedido}
    return render(request, 'food/exito.html',ctx)


#Registrarse
def signup(request):
    ctx = {'active_link':'login'}
    if request.POST: #Significa que el usuario le envia info al server
        form = NewUserForm(request.POST)
        if form.is_valid():                       #Aqui verifica validez
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:                                        #Si visita por primera vez
        form = NewUserForm()
        ctx['form'] = form
    
    return render(request, 'food/signup.html', ctx)


#Ingresar
def logIn(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)

        if user is not None and user.is_staff:  # Verificar si el usuario es administrador
            login(request, user)
            return redirect('food:admin_index')  # Redirigir al admin a la vista admin_index
        elif user is not None:
            login(request, user)
            return redirect('food:index')  # Redirigir a la vista index para usuarios normales
        else:
            messages.error(request, 'Usuario y/o contraseña incorrectos')

    ctx = {'active_link':'login'}
    return render(request, 'food/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')


def descuentos(request):
    # Lógica para la vista de descuentos
    return render(request, 'food/descuentos.html')


def historial(request):
    # Obtener todos los pedidos del usuario actual
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-date')

    # Pasar los pedidos a la plantilla
    return render(request, 'food/historial.html', {'pedidos': pedidos})


# Vista para ver todos los pedidos (solo para administrador)
@staff_member_required
def ver_pedidos(request):
    pedidos_activos = Pedido.objects.filter(estado='activo').order_by('-date')
    pedidos_finalizados = Pedido.objects.filter(estado='finalizado').order_by('-date')
    context = {'pedidos_activos': pedidos_activos, 'pedidos_finalizados': pedidos_finalizados}
    return render(request, 'food/ver_pedidos.html', context)


# Vista para gestionar descuentos (solo para administrador)
@staff_member_required
def gestionar_descuentos(request):
    if request.method == 'POST':
        form = DescuentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Descuento agregado exitosamente')
            return redirect('food:gestionar_descuentos')
    else:
        form = DescuentoForm()

    descuentos = Descuento.objects.all()
    return render(request, 'food/gestionar_descuentos.html', {'form': form, 'descuentos': descuentos})


# Vista para ver clientes (solo para administrador)
@staff_member_required
def ver_clientes(request):
    clientes = User.objects.all()
    for cliente in clientes:
        cantidad_pedidos = Pedido.objects.filter(cliente=cliente).count()
        cliente.cantidad_pedidos = cantidad_pedidos
    return render(request, 'food/ver_clientes.html', {'clientes': clientes})


# Vista para ver solicitudes de modificación (solo para administrador)
@staff_member_required
def ver_solicitudes_modificacion(request):
    # Lógica para la vista de ver solicitudes de modificación del administrador
    solicitudes = SolicitudModificacion.objects.all()
    return render(request, 'food/ver_solicitudes_modificacion.html', {'solicitudes': solicitudes})



#No muestra nada es solo para que ande el finalizar pedido de admin
def finalizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.estado = 'finalizado'
        pedido.save()
        # Redireccionar a alguna página de confirmación o a donde sea necesario
        return redirect('food:ver_pedidos')
    # Manejar el caso en que la solicitud no sea POST (opcional)
    # Esto puede ser un error o una redirección a alguna otra página



def desactivar_descuento(request, descuento_id):
    try:
        descuento = Descuento.objects.get(pk=descuento_id)
        descuento.activo = False
        descuento.save()
    except Descuento.DoesNotExist:
        # Handle the case where the discount doesn't exist
        pass  # Or display an error message

    return redirect('food:gestionar_descuentos')

def activar_descuento(request, descuento_id):
    try:
        descuento = Descuento.objects.get(pk=descuento_id)
        descuento.activo = True
        descuento.save()
    except Descuento.DoesNotExist:
        # Handle the case where the discount doesn't exist
        pass  # Or display an error message

    return redirect('food:gestionar_descuentos')

def eliminar_descuento(request, descuento_id):
    try:
        descuento = Descuento.objects.get(pk=descuento_id)
        descuento.delete()
    except Descuento.DoesNotExist:
        # Handle the case where the discount doesn't exist
        pass  # Or display an error message

    return redirect('food:gestionar_descuentos')