# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

class Reservacion(forms.Form):
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
    widget=forms.TextInput(
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
    
    def clean(self):
        cleaned_data = super(Reservacion, self).clean()
        print(self.cleaned_data)

        start_date = self.cleaned_data['fecha_ini']
        end_date = self.cleaned_data['fecha_fin']

        currentDate = datetime.now().date()

        print(type(start_date))
        print(type(end_date))
        
        if end_date <= start_date:
            raise forms.ValidationError("La fecha final debe ser despues de la fecha inicial.")
        if start_date < currentDate:
            raise forms.ValidationError("La reservacion no puede ser en fechas pasadas.")
        return super(Reservacion, self).clean()
    