# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.core import serializers
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from .models import Habitaciones, Reservaciones, Agregados, Transacciones, RelTransaccionAgregado , RelTransaccionReservacion
from .forms import Reservacion
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# @login_required(login_url="/login/")
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

# @login_required(login_url="/login/")
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

    form = Reservacion(request.POST or None, room = room_id)
    #form = Reservacion(room = room_id)

    context = {
        'data' : data,
        'room' : room,
        'reservacion': form,
        'agrega': agregados
    }  

    if request.method == 'GET':
        return HttpResponse(html_template.render(context, request))  
    if request.method == 'POST':
        if form.is_valid():
            
            form = Reservacion(None, room = room_id)

            # Reservacion object saved
            fecha_ini = datetime.strptime(request.POST['fecha_ini'],"%d/%m/%Y").strftime("%Y-%m-%d")
            fecha_fin = datetime.strptime(request.POST['fecha_fin'],"%d/%m/%Y").strftime("%Y-%m-%d")

            reserva = Reservaciones.objects.create(estado='PR', fecha_reserva = fecha_ini, fecha_entrega = fecha_fin, costo_reservado = request.POST['cost'], correo = request.POST['email'], habitaciones = room ) 
            # Transaccion object saved
            nombre = "Cliente: " + request.POST['paterno'] + " " + request.POST['materno'] + " " + request.POST['nombres']

            trans = Transacciones.objects.create(fecha_transaccion = datetime.now(), total = request.POST['cost'], detalles = nombre )

            # Trnas-Reser relation saved
            RelTransaccionReservacion.objects.create(transaccion= trans, reservacion = reserva)

            costo = float(request.POST['cost'])
            # Agregado-Trans relation saved
            for a in agregados:
                if a.agregado in request.POST:
                    costo += float(a.costo)
                    RelTransaccionAgregado.objects.create(transaccion = trans, agregado = a)

            Transacciones.objects.filter(pk = trans.pk).update(total = costo)

            # Envio de email a administrador

            confirmation_template = render_to_string('home/confirmation.html')

            subject_admin = "Reservacion Realizada"
            message_admin = "Una reservacion a sido realizada recientemente"
            email_from_admin = settings.EMAIL_HOST_USER
            recipient_list_admin = ["pedro.barrita1029@gmail.com"]
            send_mail(subject_admin, message_admin, email_from_admin, recipient_list_admin)

            # Envio de email a usuario
            subject = "Reservacion Realizada"
            message = confirmation_template
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email']]
            send_mail(subject, message, email_from, recipient_list)
            

        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def camarista(request):
    
    context = {
        
    }

    html_template = loader.get_template('home/genCam.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def mantenimiento(request):
    
    context = {
        
    }

    html_template = loader.get_template('home/genMant.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def gerente(request):
    
    context = {
        
    }

    html_template = loader.get_template('home/generalAdm.html')
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

