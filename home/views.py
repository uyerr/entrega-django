import random
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.models import Familiar
from home.forms import HumanoFormulario, BusquedaFormulario

def add_familiar(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        creacion = request.POST.get('creacion')
        familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, creacion=creacion)
        familiar.save()
        
        return redirect('ver_familiar')
    
    formulario = HumanoFormulario()
    
    return render(request, 'add_familiar.html', {'formulario': formulario})



def ver_familiar(request):
    
    nombre = request.GET.get('nombre')
    
    if nombre:
        familiares = Familiar.objects.filter(nombre__icontains=nombre)
    else:
        familiares = Familiar.objects.all()
    
    formulario = BusquedaFormulario()
    
    return render(request, 'ver_familiar.html', {'familiares': familiares, 'formulario' : formulario})

def home(request):
    
    return render(request, 'home.html')