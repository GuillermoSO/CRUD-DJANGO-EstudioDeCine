from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('directores', views.directores, name='directores'),
    path('directores/crear', views.crear_director, name='crear'),
    path('directores/editar', views.editar_director, name='editar'),
    
]