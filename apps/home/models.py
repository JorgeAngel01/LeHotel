# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Formatos

def dinero():
    return models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
    )

formato_dinero = dinero

def llave(referencia):
    return models.ForeignKey(
        referencia, blank=False,
        on_delete=models.RESTRICT,
        null=True,
    )

formato_llave = llave

# Tabla Habitaciones

class Habitaciones(models.Model):

    class estadoHabitacion(models.TextChoices):
        DISPONIBLE = 'DI', 'Disponible'
        OCUPADA = 'OC', 'Ocupada'
        MANTENIMIENTO = 'MA', 'Mantenimiento'
        LIMPIEZA = 'LI', 'Limpieza'
        DESHABILITADA = 'DE', 'Deshabilitada'

    nombre =  models.CharField(max_length=50)
    estado = models.CharField(
        max_length=2,
        choices=estadoHabitacion.choices,
        default=estadoHabitacion.DESHABILITADA,
    )
    cant_adultos = models.IntegerField(default=0)
    cant_ninos = models.IntegerField(default=0)
    costo = formato_dinero()
    informacion = models.CharField(max_length=250)
    foto_ref = models.ImageField(
        upload_to='archivos/fotos',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre

# Tabla Reservaciones

class Reservaciones(models.Model):

    class estadoReservacion(models.TextChoices):
        ACEPTADA = 'AC', 'Aceptada'
        RECHAZADA = 'RE', 'Rechazada'
        PROCESANDO = 'PR', 'Procesando'

    fecha_reserva = models.DateField()
    fecha_entrega = models.DateField(
        blank=True,
        null=True,
    )
    estado = models.CharField(
        max_length=2,
        choices=estadoReservacion.choices,
        default=estadoReservacion.PROCESANDO,
    )
    costo_reservado = formato_dinero()
    correo = models.EmailField()
    habitaciones = formato_llave(Habitaciones)

# Tabla Agregados

class Agregados(models.Model):

    class categoriaAgregado(models.TextChoices):
        DESCONOCIDA = 'DE', 'Desconocida'
        PRODUCTO = 'PR', 'Producto'
        SERVICIO = 'SE', 'Servicio'

    categoria = models.CharField(
        max_length=2,
        choices=categoriaAgregado.choices,
        default=categoriaAgregado.DESCONOCIDA,
    )
    agregado = models.CharField(max_length=50)
    costo = formato_dinero()
    descripcion = models.CharField(
        max_length=250,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.agregado

# Tabla Transacciones

class Transacciones(models.Model):

    class estadoTransaccion(models.TextChoices):
        FINALIZADA = 'FI', 'Finalizada'
        CANCELADA = 'CA', 'Cancelada'
        VALIDANDO = 'VA', 'Validando'

    class medioPago(models.TextChoices):
        EFECTIVO = 'EF', 'Efectivo'
        DEBITO = 'DE', 'Tarjeta de debito'
        CREDITO = 'CR', 'Tarjeta de credito'
        CHEQUE = 'CH', 'Cheque'
        REFERENCIA = 'RE', 'Referencia bancaria'
        TRANFERENCIA = 'TR', 'Transferencia bancaria'

    fecha_transaccion = models.DateField()
    estado = models.CharField(
        max_length=2,
        choices=estadoTransaccion.choices,
        default=estadoTransaccion.VALIDANDO,
    )
    total = formato_dinero()
    medio_pago = models.CharField(
        max_length=2,
        choices=medioPago.choices,
        default=medioPago.EFECTIVO,
    )
    detalles = models.CharField(max_length=200)

# Tabla Relacion Transaccion - Reservacion

class RelTransaccionReservacion(models.Model):
    transaccion = formato_llave(Transacciones)
    reservacion = formato_llave(Reservaciones)

# Tabla Relacion Transaccion - Agregados

class RelTransaccionAgregado(models.Model):
    transaccion = formato_llave(Transacciones)
    agregado = formato_llave(Agregados)