from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.CharFieldField('Descripción', max_length = 500, null=False)
    programa = models.TextFields('Programa Asignatura', max_length=150, null=False)
    estado = models.BooleanField('Estado del Curso', null =False)
    docente= models.ForeignKey(Docente, on_delete=models.CASCADE)
    objetivo = models.ForeignKey(Aprendizajeesperado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
        

        
class Progreso(models.Model):
    nombre = models.CharField('Progreso Estudiante', max_length=150, null=False)
    descripcion = models.CharField('Avance Estudiante',max_length= 150, null=False)
    curso = models.ForeignKey(Curso, null=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
        
class Solicitud_Estudiante(models.Model):
    nombre = models.CharField('Solicitud de Inscripcion del Curso', max_length=150, null=False)
    estado = models.BooleanField('Estado de la Solicitud', null =False)
    curso = models.ForeignKey(Curso, null=False)
    estudiante = models.ForeignKey(Estudiante, null =False)
    docente= models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre