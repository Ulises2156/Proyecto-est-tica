from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Personal, Reserva, Pago, Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def pagina_inicio(request):
    return render(request, 'login.html')

def registro(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request,'regitro.html', {'form':form})


#vistas para el cliente vamos probando
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista.clientes.html',{'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'detalle_cliente.html',{'cliente': cliente})

# vistas para el personal
def lista_personal(request):
    personal = Personal.objects.all()
    return render(request, 'lista_personal.html', {'personal': personal})

def detalle_personal(request, personal_id):
    personal = get_object_or_404(Personal, pk=personal_id)
    return render(request, 'detalle_personal.html', {'personal':personal})

# vistas para las reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html',{'reservsa': reservas})

def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request,'detalle_reserva.html', {'reserva': reserva})

# pagos
def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'lista_pagos.html', {'pagos': pagos})

def detalle_pago(request, pago_id):
    pago = get_object_or_404(Pago, pk=pago_id)
    return render(request,'detalle_pago.html', {'pago': pago})

# Productos
def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_productos(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    return render(request, 'detalle_productos.html',{'producto': producto})
