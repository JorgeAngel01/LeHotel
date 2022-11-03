# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Agregados, Habitaciones, Reservaciones
from .models import Transacciones, RelTransaccionReservacion, RelTransaccionAgregado

# Register your models here.

@admin.register(Habitaciones)
class HabitacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado', 'cant_adultos', 'cant_ninos', 'costo', 'informacion', 'foto_ref')
    list_filter = ('estado',)

@admin.register(Reservaciones)
class ReservacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_reserva', 'fecha_entrega', 'estado', 'costo_reservado','correo','habitaciones_id')
    list_filter = ('estado','fecha_reserva',)
    date_hierarchy = 'fecha_reserva'

@admin.register(Agregados)
class AgregadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'agregado','costo', 'descripcion')
    list_filter = ('categoria',)

@admin.register(Transacciones)
class TransaccionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_transaccion', 'estado', 'total','detalles')
    list_filter = ('fecha_transaccion',)
    date_hierarchy = 'fecha_transaccion'

@admin.register(RelTransaccionReservacion)
class RelTraResAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id', 'reservacion_id')

@admin.register(RelTransaccionAgregado)
class RelTraAgrAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id', 'agregado_id')