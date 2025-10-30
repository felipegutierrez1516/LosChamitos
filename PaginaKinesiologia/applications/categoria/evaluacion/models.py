from django.db import models

# Create your models here.

class Evaluacion(models.Model):
    nombre = models.CharField('Evaluacion', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente_ficticio, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    temainterrogacion = models.ForeignKey(Tema_interrogacion, on_delete=models.CASCADE)
    partedelcuerpo = models.ForeignKey(Parte_del_Cuerpo, on_delete=models.CASCADE)


    def _str_(self):
        return str(self.id) + '-' + self.nombre

    
class Respuesta_Evaluacion(models.Model):
    nombre = models.CharField('Respuesta evaluación', max_length=150, null=False)
    descripcion = models.TextField('Detalle', null=False)
    retroalimentacion = models.TextField('Retroalimentación', null=False)
    correcta = models.BooleanField('Correcta o incorrecta', null = False)
    respuestas = models.TextField('Respuesta estudiante', null= False)
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id) + '-' + self.nombre


class Envio_Docente(models.Model):
    nombre = models.CharField('Nombre de la evaluación:', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    nombreestudiante = models.TextField('Nombre estudiante:', null=False)
    fechaentrega = models.DateField('Fecha de entrega', null = False)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    respuestaevaluacion = models.ForeignKey(Respuesta_Evaluacion, on_delete=models.CASCADE)


    def _str_(self):
         return str(self.id) + '-' + self.nombre