from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField('Nombre del Docente', max_length=150, null=False)
    apellido = models.CharField('Apellido del Docente', max_length=150, null=False)
    correo = models.EmailField('Correo del Docente', max_length=150, null=False, unique=True)
    contrasena = models.CharField('Contraseña del Docente', max_length=150, null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Estudiante(models.Model):
    nombre = models.CharField('Nombre del Estudiante', max_length=150, null=False)
    apellido = models.CharField('Apellido del Estudiante', max_length=150, null=False)
    correo = models.EmailField('Correo del Estudiante', max_length=150, null=False, unique=True)
    contrasena = models.CharField('Contraseña del Estudiante', max_length=150, null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Aprendizaje_Esperado(models.Model):
    nombre = models.CharField('Nombre del Objetivo', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)

     def __str__(self):
        return str(self.id) + '-' + self.nombre

class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    programa = models.TextField('Programa Asignatura', null=False)
    estado = models.BooleanField('Estado del Curso', null = False)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    objetivo = models.ForeignKey(Aprendizaje_Esperado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Progreso(models.Model):
    nombre = models.CharField('Progreso del Estudiante', max_length=150, null=False)
    descripcion = models.TextField('Avance', null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Solicitud_Inscripcion(models.Model):
    nombre = models.CharField('Solicitud de inscripción al curso', max_length=150, null=False)
    estado = models.BooleanField('Estado del Curso', null = False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Categoria_Clinica(models.Model):
    nombre = models.CharField('Categoria Clínica', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Paciente_Ficticio(models.Model):
    nombre = models.CharField('Paciente', max_length=150, null=False)
    descripcion = models.TextField('Descripción General del Paciente', null=False)
    edad = models.IntergerField('Edad del Paciente', null=False)
    genero = models.CharField('Género del Paciente',)
    categoria = models.ForeignKey(Categoria_Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Etapas(models.Model):
    nombre = models.CharField('Etapa', max_length=150, null=False)
    descripcion = models.TextField('Descripción', null=False)
    video = models.URLField()
    pregunta = models.TextField('Pregunta', null=false)
    paciente = models.ForeignKey(Paciente_Ficticio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Tema_Interrogacion(models.Model):
    nombre = models.CharField('Tema', max_length=500, null=False)
    pregunta = models.CharField('Pregunta', max_length=500, null=False)
    respuesta = models.CharField('Respuesta', max_length=500, null=False)
     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id) + '-' + self.nombre

