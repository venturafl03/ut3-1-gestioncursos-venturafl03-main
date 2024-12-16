from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('editar_curso/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    
    path('crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/', views.lista_estudiantes, name='lista_estudiantes'),
    path('editar_estudiante/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar_estudiante/<int:estudiante_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    
    path('crear_inscripcion/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscripciones/', views.lista_inscripciones, name='lista_inscripciones'),
    path('eliminar_inscripcion/<int:inscripcion_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
