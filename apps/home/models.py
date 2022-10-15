# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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