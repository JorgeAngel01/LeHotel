# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Habitaciones, MediosPago, DatosPago

# Register your models here.

@admin.register(Habitaciones)
class HabitacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado', 'costo', 'informacion')
@admin.register(MediosPago)
class MediosPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
@admin.register(DatosPago)
class DatosPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'informacion', 'medios_id')
