from django.urls import path
from . import views

urlpatterns =[
    path('cliente/',views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('personal/', views.lista_personal, name='lista_personal'),
    path('personal/<int:personal_id>/', views.detalle_personal, name='detalle_personal'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reserva/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    path('pagos/', views.lista_pagos, name='lista_pagos'),
    path('pago/<int:pago_id>/', views.detalle_pago, name='detalle_pago'),
    path('productos/', views.lista_productos,  name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_productos, name='detalle_producto'),
    path('registro/', views.registro, name='registro'),
    ]
