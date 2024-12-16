from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudiante, Inscripcion
from .forms import CursoForm, EstudianteForm, InscripcionForm

# Vista principal
def principal(request):
    return render(request, 'blog/principal.html')

# Vista para crear un curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos') 
    else:
        form = CursoForm()
    return render(request, 'blog/crear_curso.html', {'form': form})

# Vista para la lista de cursos
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'blog/lista_curso.html', {'cursos': cursos})

# Vista para editar un curso
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos') 
    else:
        form = CursoForm(instance=curso)
    return render(request, 'blog/editar_curso.html', {'form': form, 'curso': curso})

# Vista para eliminar un curso
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('lista_cursos')  

# Vista para crear un estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')  
    else:
        form = EstudianteForm()
    return render(request, 'blog/crear_estudiante.html', {'form': form})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    print(estudiantes)
    return render(request, 'blog/lista_estudiante.html', {'estudiantes': estudiantes})

def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'blog/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    estudiante.delete()
    return redirect('lista_estudiantes')


def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscripciones') 
    else:
        form = InscripcionForm()
    return render(request, 'blog/crear_inscripcion.html', {'form': form})

def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'blog/listar_inscripciones.html', {'inscripciones': inscripciones})

def eliminar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    inscripcion.delete()
    return redirect('lista_inscripciones') 
