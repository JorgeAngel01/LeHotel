# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Reservacion(forms.Form):
    nombres = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": "Nombres",
                "class": "form-control",
                "id": "first_name",
                'required' : "true"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))    
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

