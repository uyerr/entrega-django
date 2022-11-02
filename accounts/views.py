from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as log
from accounts.forms import RegisterForm

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            log(request, user)
            
            return redirect('home')
    else:
        formulario = AuthenticationForm()
    
    
    return render(request, 'login.html', {'formulario': formulario})


def register(request):
    
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        
            return redirect('home')
    else:
        formulario = RegisterForm()
    
    
    return render(request, 'register.html', {'formulario': formulario})