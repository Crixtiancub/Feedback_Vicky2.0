from django.shortcuts import render, redirect
import os
from vicky import templates
from .models import *
from django.template.response import TemplateResponse
import requests
import json
from prueba_Vicky.settings import URL_VICKY, JWT

# Create your views here.
def home(request):

    if request.GET:
        request.session['user_Name'] = str(request.GET.get('user_Name'))      

        return render(request, 'dashboard.html')

    if request.POST:

        if 'Si' in request.POST:
            acierto = str(request.POST.get('Si'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
        
            envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )

            envio_Pregunta.save()

            contexto = {
                "continue": "continuar",
            }

            return TemplateResponse(request, 'dashboard.html', contexto)

        if 'No' in request.POST:
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
            acierto = str(request.POST.get('No'))

            context = {
                "back_pregunta": pregunta,
                "back_respuesta": respuesta,
                "acierto" : acierto,
            } 

            return TemplateResponse(request, 'dashboard.html' , context)

        if 'sugerencia' in request.POST:

            pregunta = str(request.POST.get('back_Pregunta'))
            respuesta = str(request.POST.get('back_Respuesta'))
            acierto = 'No'
            sugerencia = str(request.POST.get('sugerencia_Vicky'))

            envio_Pregunta = preguntas_Vicky(
                pregunta=pregunta,
                respuesta=respuesta,
                acierto= acierto,
                sugerencia = sugerencia
                )

            envio_Pregunta.save()

            contexto = {
                "continue": "continuar",
            }

            return TemplateResponse(request, 'dashboard.html', contexto)

        if 'continue' in request.POST:
            return render(request, 'dashboard.html')

        if 'break' in request.POST:
            return redirect('../noVisitas.html')
        
        pregunta = str(request.POST.get('pregunta_Vicky'))

        documento = {
            "pregunta": pregunta,
            "formato": "texto"
        }

        respuesta = requests.post(url=URL_VICKY,
        headers= { "Authorization": "Bearer " + JWT },
        json=documento)

        context = {
            "pregunta":pregunta,
            "respuesta":json.loads(respuesta.content)['respuesta'],
        }

        return TemplateResponse(request, 'dashboard.html' , context)

    else:       

        return render(request, 'dashboard.html')

def noVisitas(request):

    request.session['num_visitas'] = 3

    if request.POST:

        if 'comentario' in request.POST:
            nombre_Usuario = str(request.session['user_Name'])
            comentario_Usuario = str(request.POST.get('comentario'))

            user = usuario(
                usuario = nombre_Usuario,
                comentario = comentario_Usuario
            )

            user.save()

            print("Usuario guardado...")

            request.session['comentario'] = "ready"

            contexto = {
                'comentario' : request.session['comentario'],
            }

            return render(request, 'noVisitas.html', contexto)

    request.session['comentario'] = ''

    contexto = {
        'comentario' : request.session['comentario'],
    }

    print(request.session['comentario'])

    return render(request, 'noVisitas.html', contexto)

def user_Name(request):

    return render(request, 'user_Name.html')