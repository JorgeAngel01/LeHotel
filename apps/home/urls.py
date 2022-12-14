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
    path('gerente/reservaciones/', views.gerente, name='ger-res'),
    path('gerente/transacciones/', views.gerente, name='ger-trans'),
    path('gerente/habitaciones/', views.habitaciones, name='ger-hab'),
    path('gerente/ingresos/', views.ingresos, name='ger-ing'),

    path('gerente/update/<int:option>/<int:id>', views.update, name='ger-update'),
    path('gerente/delete/<int:option>/<int:id>', views.delete, name='ger-del'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
