# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('', include("apps.authentication.urls")), # Auth routes - login / register
    path('reservacion/<int:room_id>/', views.reservacion, name='reservacion'),
    path('camarista/', views.camarista, name='camarista'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('gerente/', views.gerente, name='gerente'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
