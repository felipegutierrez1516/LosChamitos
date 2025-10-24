from django.db import models

# Create your models here.
# Asumo que la entidad Docente ya está definida en otro lugar y se usa para la FK.
# class Docente(models.Model):
#     usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, primary_key=True)
#     ...

class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre