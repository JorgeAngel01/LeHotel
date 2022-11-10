# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from venv import create
from django.core import serializers
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Habitaciones, Reservaciones, Agregados
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
    
    # Room display
    room = Habitaciones.objects.get(id=room_id)

    #Room reservation
    queryset = Reservaciones.objects.filter(habitaciones=room_id, estado="AC" ).order_by('fecha_reserva')
    data = serializers.serialize('json', list(queryset))

    #Room additions
    agregados = Agregados.objects.all()

    html_template = loader.get_template('home/reservaciones.html')
    #Recibo datos 
    print(request.POST)
    form = Reservacion(request.POST or None)
    if form.is_valid():
        form = Reservacion()
        print(request.POST)
  
    """
    if request.method == 'GET':
        return HttpResponse(html_template.render(context, request))  
    else:
        print(request.POST)
        print(request.POST['email'])
        print(request.POST['nombres'])
        print(request.POST['paterno'])
        print(request.POST['materno'])
        print(request.POST['fecha_ini'])
        print(request.POST['fecha_fin'])
        for a in agregados:
            if a.agregado in request.POST: print(request.POST[a.agregado])


        fecha_ini = datetime.strptime(request.POST['fecha_ini'],"%m/%d/%Y").strftime("%Y-%m-%d")
        fecha_fin = datetime.strptime(request.POST['fecha_fin'],"%m/%d/%Y").strftime("%Y-%m-%d")

        reserva = Reservaciones.objects.create(estado='PR', fecha_reserva = fecha_ini, fecha_entrega = fecha_fin, costo_reservado = request.POST['cost'], correo = request.POST['email'], habitaciones = room ) 
    """
    context = {
        'data' : data,
        'room' : room,
        'reservacion': form,
        'agrega': agregados
    }  
    
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
