from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'), 
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'), 
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'), 
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'), 
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'), 
    path('estudiantes/editar/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'), 
    path('estudiantes/eliminar/<int:estudiante_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('inscripciones/', views.lista_inscripciones, name='lista_inscripciones'),
    path('inscripciones/crear/', views.crear_inscripcion, name='crear_inscripcion'), 
    path('inscripciones/eliminar/<int:inscripcion_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),  
]

