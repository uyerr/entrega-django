from django.urls import path
from advanced import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name="ver_mascotas"),
    path('mascotas/crear/', views.crear_mascota, name="crear_mascota"),
]
