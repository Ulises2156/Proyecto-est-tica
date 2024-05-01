from django.db import models
from django.utils import timezone

class Personal(models.Model):
    ROL_CHOICES=(
        ('Peluquero', 'Peluquero'),
        ('Administrador', 'Administrador')
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    personal_asignado = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha_hora_reserva = models.DateTimeField(default=timezone.now)
    servicio_solicitado = models.CharField(max_length=100)
    estado_reserva = models.CharField(max_length=20)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} {self.cliente.apellido}"

class Pago(models.Model):
    reserva_asociada = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora_pago = models.DateField(default=timezone.now)

    def __str__(self):
        return F"Pago finalizado de {self.monto} para {self.reserva_asociada}"

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion= models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()

    def __str__(self):
        return self.nombre
        