from django.db import models

# Create your models here.
class Parte_del_Cuerpo(models.Model):
    nombre = models.CharField('Parte del Cuerpo', max_length=150, null=False)
    parte = models.TextField('Parte Seleccionada', null=False)
    etapa= models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre