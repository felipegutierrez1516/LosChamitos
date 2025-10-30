from django.db import models
class Paciente_Ficticio(models.Model):
    nombre = models.CharField('Paciente', max_length=150, null=False)
    descripcion = models.TextField('Descripción General del Paciente', null=False)
    edad = models.IntergerField('Edad del Paciente', null=False)
    genero = models.CharField('Género del Paciente',)
    categoria = models.ForeignKey(Categoria_Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
