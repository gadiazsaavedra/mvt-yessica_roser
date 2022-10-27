from sqlite3 import Timestamp
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares
from datetime import datetime

# Create your views here.

def agregar_familiar(request, nombre, apellido, edad, fecha_nacimiento, parentesco):
    integrante = Familiares(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento, parentesco=parentesco)
    fecha_nacimiento = datetime.strptime('%d/%m/%Y', "fecha_nacimiento")
    integrante.save()

    return HttpResponse('lista_familiares')
   
    
def lista_familiares(request):
    
    lista =  Familiares.objects.all()

    return render(request, "lista_familiares.html", {"lista_familiares":lista})

