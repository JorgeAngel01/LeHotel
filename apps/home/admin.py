# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Agregados, Habitaciones, MediosPago, DatosPago, Reservaciones
from .models import Transacciones, RelTransaccionReservacion, RelTransaccionAgregado

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

@admin.register(Reservaciones)
class ReservacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_reservada', 'costo_reservado','correo','datos_pago_id','habitaciones_id')

@admin.register(Agregados)
class AgregadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'agregado','costo')

@admin.register(Transacciones)
class TransaccionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_transaccion', 'total','detalles')

@admin.register(RelTransaccionReservacion)
class RelTraResAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id', 'reservacion_id')

@admin.register(RelTransaccionAgregado)
class RelTraAgrAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id', 'agregado_id')