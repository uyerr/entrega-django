from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as log
from accounts.forms import RegisterForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from accounts.models import ExtensionUsuario


# Create your views here.
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            log(request, user)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            
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


@login_required
def profile(request):
    
    extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
    
    return render(request, 'profile.html', {})


@login_required
def edit_profile(request):
    
    user = request.user
    
    if request.method == 'POST':
       formulario = ProfileEditForm(request.POST, request.FILES)
       
       if formulario.is_valid():
           data = formulario.cleaned_data
           
           user.first_name = data['first_name']
           user.last_name = data['last_name']
           user.email = data['email']
           user.extensionusuario.avatar = data['avatar']
           
           user.extensionusuario.save()
           request.user.save()
           
           return redirect('profile')
    else:   
        formulario = ProfileEditForm(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': user.extensionusuario.avatar,
            }
        )
    
    return render(request, 'edit_profile.html', {'formulario': formulario})


class password(LoginRequiredMixin, PasswordChangeView):
    
    template_name = 'password.html'
    success_url = 'profile/'