from django.shortcuts import redirect, render
from advanced.models import Mascota
from advanced.forms import MascotaFormulario, BusquedaFormulario


# Create your views here.
def ver_mascotas(request):
    
    nombre = request.GET.get('nombre')
    
    if nombre:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre)
    else:
        mascotas = Mascota.objects.all()
    
    formulario = BusquedaFormulario()
    
    return render(request, 'ver_mascotas.html', {'mascotas': mascotas, 'formulario' : formulario})

def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            mascota = Mascota(
                nombre=data['nombre'],
                especie=data['especie'],
                edad=data['edad'],
                nacimiento=data['nacimiento'],
            )
            mascota.save()
            
            return redirect('ver_mascotas') 
            
    formulario = MascotaFormulario() 
    
    return render(request, 'crear_mascota.html', {'formulario': formulario})