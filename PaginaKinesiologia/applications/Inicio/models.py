from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre