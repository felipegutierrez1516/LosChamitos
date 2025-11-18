from django.db import models
from applications.Caso_Clínico.models import *

# Create your models here.

class Tema_Interrogacion(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    nombre = models.CharField('Tema', max_length=500)
    pregunta = models.CharField('Pregunta', max_length=500)
    respuesta = models.CharField('Respuesta', max_length=500)
    dificultad = models.CharField('Dificultad', max_length=10, choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')])

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    class Meta:
        verbose_name = 'Tema de Interrogación'
        verbose_name_plural = 'Temas de Interrogación'
        ordering = ['nombre']