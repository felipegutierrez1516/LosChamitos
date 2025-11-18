from django.db import models
from applications.Cursos.models import *

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    apellido = models.CharField('Apellido', max_length=150)
    correo = models.EmailField('Correo electrónico', max_length=150, unique=True)
    contrasena = models.CharField('Contraseña', max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['nombre']


class Progreso(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    descripcion = models.TextField('Avance')
    porcentaje_avance = models.FloatField('Porcentaje de avance')
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Progreso'
        verbose_name_plural = 'Progresos'
        ordering = ['id']


class Solicitud_Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    estado = models.CharField('Estado', max_length=10, choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')])
    comentario = models.TextField('Comentario del estudiante', blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Solicitud de Inscripción'
        verbose_name_plural = 'Solicitudes de Inscripción'
        ordering = ['id']
