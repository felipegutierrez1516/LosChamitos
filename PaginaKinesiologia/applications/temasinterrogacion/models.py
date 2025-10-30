from django.db import models

class Tema_Interrogacion(models.Model):
    nombre = models.CharField('Tema', max_length=500, null=False)
    pregunta = models.CharField('Pregunta', max_length=500, null=False)
    respuesta = models.CharField('Respuesta', max_length=500, null=False)
     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id) + '-' + self.nombre

