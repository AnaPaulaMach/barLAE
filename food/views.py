from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hamburguesa, Bebida, Pedido, Item
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm
from django.contrib import messages
import random
import json

def randomOrderNumber(length): # El numero de orden sera random
    sample  = 'ABCDEFGH0123456789'
    numeroO =''.join((random.choice(sample) for i in range(length)))
    return numeroO 

# Create your views here. View es una funcion de python

def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link':'index'}
    return render(request, 'food/index.html', ctx)
#la funcion render tranfroma el codigo html a httpresponse

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
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': #is_ajax ya no se usa
        request.session['note'] = request.POST.get('note')  # note es el comentario
        request.session['pedido'] = request.POST.get('pedidos')  
        pedidos = json.loads(request.session['pedido'])
        request.session['cuenta'] = request.POST.get('cuenta')  
        randomNum = randomOrderNumber(6)

        while Pedido.objects.filter(numero=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            pedido = Pedido(cliente=request.user,
                            numero=randomOrderNumber(6),
                            cuenta=float(request.session['cuenta']),
                            note=request.session['note'] )
            pedido.save()
            request.session['pedidoNum'] = pedido.numero
            for articulo in pedidos:
                item = Item(
                    pedido = pedido,
                    nombre = articulo[0],
                    precio = float(articulo[2]),
                    size   = articulo[1],
                )
                item.save()

    ctx = {'active_link':'pedido'}
    return render(request, 'food/pedido.html', ctx)

#session para guardar info que son similares a local storage
# son diccionarios , tienen expire time
# 0 significa que van a expirar cuando se cierre el navegador


#Vista succes para cuando un cliente realice su orden
def exito(request):
    pedidoNum = request.session['pedidoNum']
    cuenta = request.session['cuenta'] 
    items = Item.objects.filter(pedido__numero = pedidoNum)
    ctx = {'pedidoNum':pedidoNum, 'cuenta':cuenta, 'items':items}
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

        if user is not None:        #si existe en la BD
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Usuario y/o contraseña incorrecto')

    ctx = {'active_link':'login'}
    return render(request, 'food/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')