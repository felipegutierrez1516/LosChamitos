from django.db import models
from applications.Cursos.models import *

# Create your models here.

class Paciente_Ficticio(models.Model):
    nombre = models.CharField('Nombre del Paciente', max_length=150)
    descripcion = models.TextField('Descripción General')
    edad = models.IntegerField('Edad')
    genero = models.CharField('Género', max_length=50)
    categoria = models.ForeignKey(Categoria_Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    class Meta:
        verbose_name = 'Paciente Ficticio'
        verbose_name_plural = 'Pacientes Ficticios'
        ordering = ['nombre']



class Etapa(models.Model):
    nombre = models.CharField('Nombre de la Etapa', max_length=150)
    descripcion = models.TextField('Descripción')
    video = models.URLField('Video')
    pregunta = models.TextField('Pregunta')
    paciente = models.ForeignKey(Paciente_Ficticio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'
        ordering = ['nombre']


class Partes_del_Cuerpo(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    nombre = models.CharField('Parte del cuerpo', max_length=150)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen', upload_to='partes_cuerpo/')
    ubicacion_anatomica = models.CharField('Ubicación anatómica', max_length=150)
    funcion = models.TextField('Función', blank=True)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    class Meta:
        verbose_name = 'Parte del Cuerpo'
        verbose_name_plural = 'Partes del Cuerpo'
        ordering = ['nombre']