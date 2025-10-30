from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    programa = models.TextField('Programa de asignatura', null=False)
    estado = models.BooleanField('Estado del curso', null=False)
    docente = models.ForeignKey('Docentes', on_delete=models.CASCADE)
    objetivo = models.ForeignKey('Aprendizajeesperado', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre



class Progreso(models.Model):
    nombre = models.CharField('Progreso del Estudiante', max_length=150, null=False)
    descripcion = models.TextField('Avance', null=False)
    curso = models.ForeignKey('Cursos', on_delete=models.CASCADE)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Solicitud_inscripcion(models.Model):
    nombre = models.CharField('Solicitud de Inscripcion', max_length=150, null=False)
    estado = models.BooleanField('Estado de Inscripcion', null=False)    
    curso = models.ForeignKey('Cursos', on_delete=models.CASCADE)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    docente = models.ForeignKey('Docentes', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + '-' + self.nombre
