import random
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from home.models import Familiar

def add_familiar(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), creacion=datetime.now())
        familiar.save()
        
        return redirect('ver_familiar')
    
    return render(request, 'add_familiar.html', {})

def ver_familiar(request):
    
    familiares = Familiar.objects.all()
    
    # template = loader.get_template('ver_familiar.html')
    # render_template = template.render({'familiares': familiares})
    
    # return HttpResponse(render_template)
    
    return render(request, 'ver_familiar.html', {'familiares': familiares})