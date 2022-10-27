from django.shortcuts import redirect, render
from advanced.models import Mascota
from advanced.forms import MascotaFormulario, BusquedaFormulario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
        else:
            return render(request, 'crear_mascota.html', {'formulario': formulario})
        
    formulario = MascotaFormulario() 
    
    return render(request, 'crear_mascota.html', {'formulario': formulario})

def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            mascota.nombre = data['nombre']
            mascota.especie = data['especie']
            mascota.edad = data['edad']
            mascota.nacimiento = data['nacimiento']
            
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'editar_mascota.html', {'formulario': formulario, 'mascota': mascota})
        
    formulario = MascotaFormulario(
        initial={
            'nombre': mascota.nombre,
            'especie': mascota.especie,
            'edad': mascota.edad,
            'nacimiento': mascota.nacimiento
        }
    ) 
    
    return render(request, 'editar_mascota.html', {'formulario': formulario, 'mascota': mascota})

def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    
    return redirect('ver_mascotas')


class ListaMascotas(ListView):
    model = Mascota
    template_name = 'ver_mascotas_cbv.html'

class CrearMascota(CreateView):
    model = Mascota
    success_url = '/mascotas/'
    template_name = 'crear_mascota_cbv.html'
    fields = ['nombre', 'especie', 'edad', 'nacimiento']
    
class EditarMascota(UpdateView):
    model = Mascota
    success_url = '/mascotas/'
    template_name = 'crear_mascota_cbv.html'
    fields = ['nombre', 'especie', 'edad', 'nacimiento']

class EliminarMascota(DeleteView):
    model = Mascota
    success_url = '/mascotas/'
    template_name = 'eliminar_mascota_cbv.html'