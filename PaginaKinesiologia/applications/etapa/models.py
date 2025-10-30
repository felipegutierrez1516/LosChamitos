from django.db import models
class Etapas(models.Model):
    nombre = models.CharField('Etapa', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    video = models.URLField()
    pregunta = models.TextField('Pregunta', null=false)
    paciente = models.ForeignKey(Paciente_Ficticio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

