from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def clean(self):
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField(null=False)

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser una fecha futura.")

        if (date.today() - self.fecha_nacimiento).days < 18 * 365:
            raise ValidationError("El estudiante debe tener al menos 18 años.")

    def __str__(self):
        return self.nombre
    

class Inscripcion(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)  
    fecha_inscripcion = models.DateField(null=False) 

    def clean(self):
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día actual.")
        
    #     if self.fecha_inscripcion > self.curso.fecha_fin:
    #         raise ValidationError("El estudiante no puede inscribirse en un curso que ya ha finalizado.")
        
    #     if self.curso.fecha_fin < date.today():
    #         raise ValidationError("El curso ya ha finalizado, no es posible inscribir al estudiante.")

    def __str__(self):
        return f"{self.estudiante.nombre} inscrito en {self.curso.nombre}"
