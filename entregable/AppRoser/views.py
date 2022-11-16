
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Integrante
from datetime import datetime

# Create your views here.

def base(request):
    return redirect(index)


def mostrar(request):
    data = {
        'data' : Integrante.objects.all(),
    }
    return render(request, 'mostrar.html', data)


def crear(request, dni : int = None, nombre : str = None, apellido = None):
    if nombre is None or apellido is None or dni is None:
        return redirect(index)

    integrante = Integrante(nombre = nombre, apellido = apellido, dni = dni, alta = datetime.now())
    integrante.save()

    data = {'titulo': 'Familiar creado', 'subtitulo': f'{apellido}, {nombre}'}
    return render(request, 'crear.html', data)


def index(request):
    data = {
        'titulo' : 'Nuestro Primer MVT',
        'subtitulo' : 'Agenda Familiar',
    }
    return render(request, 'index.html', data)

