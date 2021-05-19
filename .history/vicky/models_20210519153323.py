from django.db import models

# Create your models here.

class preguntas_Vicky(models.Model):
    pregunta = models.TextField(max_length=100)
    respuesta = models.TextField(max_length=200)
    acierto = models.TextField(max_length=10)
    sugerencia = models.TextField(max_length=100, default='null')

class usuario(models.Model):
    usuario = models.TextField(max_length=100)
    comentario = models.TextField(max_length=200)
    