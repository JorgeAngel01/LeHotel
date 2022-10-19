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

    def __str__(self):
        return self.nombre

# Tabla Medios de Pago

class MediosPago(models.Model):
    descripcion=models.CharField(
        max_length=100,
        blank=False,
    )

    def __str__(self):
        return self.descripcion

# Tabla Datos de Pago

class DatosPago(models.Model):
    informacion = models.CharField(
        max_length=250,
        default='Sin datos de pago',
    )
    medios = formato_llave(MediosPago)

    def __str__(self):
        return self.informacion

# Tabla Reservaciones

class Reservaciones(models.Model):
    fecha_reserva = models.DateField()
    fecha_entrega = models.DateField(
        blank=True,
        null=True,
    )
    costo_reservado = formato_dinero()
    correo = models.EmailField()
    habitaciones = formato_llave(Habitaciones)
    datos_pago = formato_llave(DatosPago)

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

    def __str__(self):
        return self.agregado

# Tabla Transacciones

class Transacciones(models.Model):
    fecha_transaccion = models.DateField()
    total = formato_dinero()
    detalles = models.CharField(max_length=200)

# Tabla Relacion Transaccion - Reservacion

class RelTransaccionReservacion(models.Model):
    transaccion = formato_llave(Transacciones)
    reservacion = formato_llave(Reservaciones)

# Tabla Relacion Transaccion - Agregados

class RelTransaccionAgregado(models.Model):
    transaccion = formato_llave(Transacciones)
    agregado = formato_llave(Agregados)