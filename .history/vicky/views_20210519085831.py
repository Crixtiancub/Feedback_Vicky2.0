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

        print(request.session['user_Name'])

        request.session['num_visitas'] = 3

        contexto = {
            "num_visitas": request.session['num_visitas'],
        }        

        return render(request, 'dashboard.html' , contexto)

    if request.POST:

        if 'Si' in request.POST:

            request.session['num_visitas'] -= 1

            acierto = str(request.POST.get('Si'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
        
            envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                "num_visitas": request.session['num_visitas'],
            }

            if request.session['num_visitas'] == 0:

                request.session['num_visitas'] = 3

                return redirect('../noVisitas')  

            return TemplateResponse(request, 'dashboard.html' , context)

        if 'No' in request.POST:

            request.session['num_visitas'] -= 1

            acierto = str(request.POST.get('No'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))

            envio_Pregunta = preguntas_Vicky(
                pregunta=pregunta,
                respuesta=respuesta,
                acierto= acierto
                )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                "num_visitas": request.session['num_visitas'],
            }

            print(context)

            if request.session['num_visitas'] == 0:

                request.session['num_visitas'] = 3

                return redirect('../noVisitas')  

            return TemplateResponse(request, 'dashboard.html' , context)

        
        pregunta = str(request.POST.get('pregunta_Vicky'))

        documento = {
            "pregunta": pregunta,
            "formato": "texto"
        }

        respuesta = requests.post(url=URL_VICKY,
        headers= { "Authorization": "Bearer " + JWT },
        json=documento)

        # respuesta = model.run_model(pregunta, user_name= request.session['user_Name'])

        context = {
            "pregunta":pregunta,
            "respuesta":json.loads(respuesta.content)['respuesta'],
            "num_visitas": request.session['num_visitas'],
        }

        print(context)

        return TemplateResponse(request, 'dashboard.html' , context)

    else:
       
        contexto = {
            "num_visits": request.session['num_visits'],
        }        

        return render(request, 'dashboard.html', contexto)

def noVisitas(request):

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