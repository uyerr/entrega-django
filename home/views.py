import random
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render
from home.models import Familiar

def add_familiar(request, nombre, apellido):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), creacion=datetime.now())
    familiar.save()
    
    # template = loader.get_template('add_familiar.html')
    # render_template = template.render({'familiar': familiar,})
    
    # return HttpResponse(render_template)
    
    return render(request, 'home/add_familiar.html', {'familiar': familiar,})

def ver_familiar(request):
    
    familiares = Familiar.objects.all()
    
    # template = loader.get_template('ver_familiar.html')
    # render_template = template.render({'familiares': familiares})
    
    # return HttpResponse(render_template)
    
    return render(request, 'home/ver_familiar.html', {'familiares': familiares})