from django.db import models
class Categoria_Clinica(models.Model):
    nombre = models.CharField('Categoria Clínica', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

