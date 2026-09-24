from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
# Create your views here.

# def inicio(request):
#     return HttpResponse("Hola, esta es mi App de Tareas")

def inicio(request):
    tareas = Tarea.objects.all()

    return render(request, 'tareasapp/inicio.html', {
        'tareas': tareas
    }) 

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        completada = 'completa' in request.POST

        Tarea.objects.create(
            titulo = titulo, 
            descripcion = descripcion,
            completada = completada

        )
        return redirect('inicio')
    return render (request, 'tareasapp/crear.html')