from django.db import models

# Create your models here.

class Parte_del_Cuerpo(models.Model):
    nombre = models.CharField('Parte del Cuerpo:', max_length=150, null=False)
    descripcion = models.CharField('descripcion', max_length=150, null=False)
    etapa = models.ForeignKey('Etapa', null=False)
    imagen = models.ImageField()

    def __str__(self):
        return str(self.id) + '-' + self.nombre

