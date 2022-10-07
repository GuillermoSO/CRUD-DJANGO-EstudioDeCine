from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('directores', views.directores, name='directores'),
    path('directores/crear', views.crear_director, name='crear'),
    path('directores/editar', views.editar_director, name='editar'),
    path('eliminar/<int:id>', views.eliminar_director, name='eliminar'),
    path('directores/editar/<int:id>', views.editar_director, name='editar'),
    
]