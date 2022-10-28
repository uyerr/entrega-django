from django.urls import path
from advanced import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name="ver_mascotas"),
    # path('mascotas/crear/', views.crear_mascota, name="crear_mascota"),
    # path('mascotas/editar/<id>', views.editar_mascota, name="editar_mascota"),
    # path('mascotas/eliminar/<id>', views.eliminar_mascota, name="eliminar_mascota"),
    
    #clases basadas en vistas
    # path('mascotas/', views.ListaMascotas.as_view(), name="ver_mascotas"),
    path('mascotas/crear/', views.CrearMascota.as_view(), name="crear_mascota"),
    path('mascotas/editar/<pk>', views.EditarMascota.as_view(), name="editar_mascota"),
    path('mascotas/eliminar/<pk>', views.EliminarMascota.as_view(), name="eliminar_mascota"),
]
