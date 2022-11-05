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
            "data-datepicker": "",
            "placeholder": "mm/dd/yyyy",
            "class": "form-control"
        }
    ))

    fecha_fin = forms.DateField(
    widget=forms.DateInput(
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
    """
    def clean_fecha_ini(self,*args,**kwargs):
        start_date = self.cleaned_data['fecha_ini']


        print(start_date)
        
        if start_date:
            raise forms.ValidationError("End date must be later than start date")
        return start_date
    """
    
    def clean(self):
        start_date = self.cleaned_data['fecha_ini']
        end_date = self.cleaned_data['fecha_fin']

        print(type(start_date))
        print(type(end_date))
        
        if end_date <= start_date:
            print("whyyyyyyyyyyyy")
            raise forms.ValidationError("End date must be later than start date")
        return super(Reservacion, self).clean()
    