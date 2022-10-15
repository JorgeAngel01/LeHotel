# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Tabla Habitaciones

class Habitaciones(models.Model):

    class estadoHabitacion(models.TextChoices):
        DISPONIBLE = 'DI', 'disponible'
        OCUPADA = 'OC', 'ocupada'
        MANTENIMIENTO = 'MA', 'mantenimiento'
        LIMPIEZA = 'LI', 'limpieza'
        DESHABILITADA = 'DE', 'deshabilitada'

    nombre =  models.CharField(
        max_length=50,
        blank=False,
    )
    estado = models.CharField(
        max_length=2,
        choices=estadoHabitacion.choices,
        default=estadoHabitacion.DESHABILITADA,
    )
    costo = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
    )
    informacion = models.CharField(max_length=250)

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
    medios = models.ForeignKey(
        MediosPago, blank=False,
        on_delete=models.RESTRICT,
    )