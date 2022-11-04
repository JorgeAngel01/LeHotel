# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Reservacion(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ingresa tus email",
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
    widget=forms.TextInput(
        attrs={
            "data-datepicker": "",
            "placeholder": "mm/dd/yyyy",
            "class": "form-control"
        }
    ))

    fecha_fin = forms.DateField(
    widget=forms.TextInput(
        attrs={
            "data-datepicker": "",
            "placeholder": "mm/dd/yyyy",
            "class": "form-control"
        }
    ))
    
    cost = forms.FloatField(
    widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "hidden": True
        }
    ))

    def clean(self):
        start_date = self.cleaned_data['fecha_ini']
        end_date = self.cleaned_data['fecha_fin']

        print(start_date)
        print(end_date)
        
        if end_date <= start_date:
            raise forms.ValidationError("End date must be later than start date")
        return super(Reservacion, self).clean()
