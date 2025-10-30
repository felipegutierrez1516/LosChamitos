from django.db import models

# Create your models here.


class Docentes(models.Model):


    nombre = models.CharField('Nombre del Docente', max_length=150, null=False)
    apellido = models.CharField('Apellido del Docente', max_length=150, null=False)
    correo = models.EmailField('Correo del Docente', max_length=150, null=False, unique=True)
    contrasena = models.CharField('Contraseña', max_length=150, null=False)


    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Estudiante(models.Model):
    nombre = models.CharField('Nombre del Estudiante', max_length=150, null=False)
    apellido = models.CharField('Apellido del Estudiante', max_length=150, null=False)
    correo = models.EmailField('Correo del Estudiante', max_length=150, null=False, unique=True)
    contrasena = models.CharField('Contraseña', max_length=150, null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
class Aprendizajeesperado(models.Model):
    nombre = models.CharField('Objetivo', max_length=150, null=False)
    descripcion = models.CharField('Nombre del Curso', max_length=150, null=False)


    def __str__(self):
        return str(self.id) + '-' + self.nombre       
class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.CharField('Descripción', max_length = 500, null=False)
    programa = models.TextField('Programa Asignatura', max_length=150, null=False)
    estado = models.BooleanField('Estado del Curso', null =False)

    docente= models.ForeignKey(Docentes, on_delete=models.CASCADE)

    docente= models.ForeignKey('Docente', on_delete=models.CASCADE)

    objetivo = models.ForeignKey('Aprendizajeesperado', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
        

        
class Progreso(models.Model):
    nombre = models.CharField('Progreso Estudiante', max_length=150, null=False)
    descripcion = models.CharField('Avance Estudiante',max_length= 150, null=False)
    curso = models.ForeignKey('Curso', null=False)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
        
class Solicitud_Estudiante(models.Model):
    nombre = models.CharField('Solicitud de Inscripcion del Curso', max_length=150, null=False)
    estado = models.BooleanField('Estado de la Solicitud', null =False)
    curso = models.ForeignKey('Curso', null=False)
    estudiante = models.ForeignKey('Estudiante', null =False)

    docente= models.ForeignKey(Docentes, on_delete=models.CASCADE)

    docente= models.ForeignKey('Docente', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + '-' + self.nombre
        
class Categoria(models.Model):
    nombre = models.CharField('Categoria Clinica', max_length=150, null=False)
    descripcion = models.CharField('Descripción', max_length= 500 , null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre
        
class Paciente_Ficticio(models.Model):
    nombre = models.CharField('Nombre del Paciente', max_length=150, null=False)
    descripcion = models.CharField('Descripción general del Paciente', max_length= 500, null=False)
    edad = models.IntegerField('Edad del Paciente', null=False)
    genero = models.CharField('Genero del Paciente', max_length=150, null=False)
    categoria = models.ForeignKey('Categoria', on_delete =models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Etapa(models.Model):
    nombre = models.CharField('Nombre Etapa', max_length=150, null=False)
    descripcion = models.CharField('Descripción', max_length= 500, null=False)
    video = models.URLField()
    paciente = models.ForeignKey('Paciente_Ficticio',on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Tema_Interrogacion(models.Model):
    nombre = models.CharField('Tema', max_length=150, null=False)
    pregunta = models.CharField('Preguntas', max_length=150, null=False)
    respuesta = models.CharField('Respuesta', null=False, max_length = 500)
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)

    

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
