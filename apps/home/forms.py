# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from .models import Reservaciones, Transacciones
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.forms import ModelForm

class Reservacion(forms.Form):
    query = None
    
    def __init__(self, *args, **kwargs):
       
        room = kwargs.pop('room')
        super(Reservacion, self).__init__(*args, **kwargs)
        self.query = Reservaciones.objects.filter(habitaciones = room , estado="AC" ).order_by('fecha_reserva') 


    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ingresa tu email",
                "class": "form-control"
            }
        )) 

    nombres = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": "Ingresa tus nombres",
                "class": "form-control"
            }
        ))       
    
    paterno = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresa tu apellido paterno",
                "class": "form-control"
            }
        )) 

    materno = forms.CharField(
    widget=forms.TextInput(
        attrs={
            "placeholder": "Ingresa tu apellido materno",
            "class": "form-control"
        }
    )) 

    fecha_ini = forms.DateField( 
    widget=forms.DateInput(
        attrs={
            "id": "fecha_ini",
            "data-datepicker": "",
            "placeholder": "dd/mm/yyyy",
            "class": "form-control"
        }
    ))

    fecha_fin = forms.DateField(     
    widget=forms.DateInput(
        attrs={
            "id": "fecha_fin",
            "data-datepicker": "",
            "placeholder": "dd/mm/yyyy",
            "class": "form-control"
        }
    ))
    
    # Hidden fields
    cost = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "hidden": True
        }
    ))
    """
    def clean_fecha_ini(self,*args,**kwargs):
        start_date = self.cleaned_data['fecha_ini']


        print(start_date)
        
        if start_date:
            raise forms.ValidationError("End date must be later than start date")
        return start_date
    """
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean(self):

        cleaned_data = super(Reservacion, self).clean()
        print(self.cleaned_data)

        start_date = self.cleaned_data['fecha_ini']
        end_date = self.cleaned_data['fecha_fin']

        dates = [start_date + timedelta(days=x) for x in range(((end_date + timedelta(1))-start_date).days)]
        print(dates)
        print(self.query)

        for obj in self.query:

            fechas = [obj.fecha_reserva + timedelta(days=x) for x in range(((obj.fecha_entrega + timedelta(1)) -obj.fecha_reserva).days)]
            print(fechas)

            if set(fechas) & set(dates):
                raise forms.ValidationError("La reservacion no puede ser en fechas ocupadas.")

        currentDate = datetime.now().date()

        print(start_date)
        print(end_date)
        
        if end_date < start_date:
            raise forms.ValidationError("La fecha final debe ser despues de la fecha inicial.")
        if start_date < currentDate:
            raise forms.ValidationError("La reservacion no puede ser en fechas pasadas.")

        return super(Reservacion, self).clean()

class ReservacionM(ModelForm):
    class Meta:
        model = Reservaciones
        fields = ['fecha_reserva', 'fecha_entrega', 'estado', 'costo_reservado', 'correo', 'habitaciones']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'costo_reservado': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.Select(attrs={'class': 'form-select'}),
        }

class Transaccion(ModelForm):
    class Meta:
        model = Transacciones
        fields = ['fecha_transaccion', 'estado', 'total', 'medio_pago', 'detalles']
        widgets = {
            'fecha_transaccion': forms.DateInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'medio_pago': forms.Select(attrs={'class': 'form-select'}),
            'detalles': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        