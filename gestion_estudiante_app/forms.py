from django import forms
from .models import Curso, Estudiante, Inscripcion
from django.core.exceptions import ValidationError
from datetime import date

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin']

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")
        return cleaned_data

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'fecha_nacimiento']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Estudiante.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
        
        edad = date.today().year - fecha_nacimiento.year
        if edad < 18:
            raise ValidationError("El estudiante debe tener al menos 18 años.")
        return fecha_nacimiento

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']

    def clean(self):
        fecha_inscripcion = self.cleaned_data.get('fecha_inscripcion')
        curso = self.cleaned_data.get('curso')
        estudiante = self.cleaned_data.get('estudiante')

        if fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día de hoy.")

        if fecha_inscripcion > curso.fecha_fin:
            raise ValidationError("El curso ya ha finalizado, no se puede inscribir en este curso.")

        if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
            raise ValidationError("El estudiante ya está inscrito en este curso.")

        return cleaned_data
