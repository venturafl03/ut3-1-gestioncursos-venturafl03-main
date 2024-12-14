from django.contrib import admin

# Register your models here.

from .models import Curso
from .models import Estudiante
from .models import Inscripcion

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)