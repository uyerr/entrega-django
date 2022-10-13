from django.urls import path
from home import views

urlpatterns = [
    path('ver-familiar', views.ver_familiar, name="ver_familiar"),
    path('crear-familiar/', views.add_familiar, name="add_familiar"),
    path('', views.home, name="home"),
]
 
