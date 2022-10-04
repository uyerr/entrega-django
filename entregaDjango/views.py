from re import template
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render

def home(request):
    
    rfile = open(r'C:\coderhouse\entrega-django\templates\index.html', 'r')
    template = Template(rfile.read())
    rfile.close()
    
    contexto = Context()
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)