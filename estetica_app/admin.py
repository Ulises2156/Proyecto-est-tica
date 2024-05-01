from django.contrib import admin
from . models import Cliente, Personal, Reserva, Pago, Productos

admin.site.register(Cliente)
admin.site.register(Personal)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Productos)

# Register your models here.
