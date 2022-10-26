# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Habitaciones, Reservaciones
from .forms import Reservacion


@login_required(login_url="/login/")
def index(request):
    
    cuartos = Habitaciones.objects.filter(estado='DI')
    
    rooms = []
    a = []
    
    for index, item in enumerate(cuartos):
        if index % 3 == 0 and index != 0:
            rooms.append(a)
            a = []
        a.append(item)
    if a : rooms.append(a)

    context = {
        'rooms': rooms,
        'cuartos' : cuartos
        }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def reservacion(request, room_id):
    
    room = Habitaciones.objects.get(id=room_id)
    reservas = Reservaciones.objects.filter(habitaciones=room_id).order_by('fecha_reserva')


    queryset = Reservaciones.objects.filter(habitaciones=room_id).order_by('fecha_reserva')
    data = serializers.serialize('json', list(queryset))
    print("fuck")
    print(data)

    context = {
        'data' : data,
        'room' : room,
        'reservacion': Reservacion()
    }

    html_template = loader.get_template('home/reservaciones.html')
    return HttpResponse(html_template.render(context, request))    


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
