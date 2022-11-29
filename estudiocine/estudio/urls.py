from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    # DIRECTORES
    path('directores', views.directores, name='directores'),
    path('directores/crear', views.crear_director, name='crearD'),
    path('directores/editar', views.editar_director, name='editarD'),
    path('eliminar/<int:id>', views.eliminar_director, name='eliminarD'),
    path('directores/editar/<int:id>', views.editar_director, name='editarD'),
    # GUIONISTAS
    path('guionistas', views.guionistas, name='guionistas'),
    path('guionistas/crear', views.crear_guionista, name='crearG'),
    path('guionistas/editar', views.editar_guionista, name='editarG'),
    path('guionistas/<int:id>', views.eliminar_guionista, name='eliminarG'),
    path('guionistas/editar/<int:id>', views.editar_guionista, name='editarG'),
    # PELICULAS
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/crear', views.crear_pelicula, name='crearP'),
    path('peliculas/editar', views.editar_pelicula, name='editarP'),
    path('peliculas/<int:id>', views.eliminar_pelicula, name='eliminarP'),
    path('peliculas/editar/<int:id>', views.editar_pelicula, name='editarP'),
    # REPORTE
    path('peliculas_pdf', views.peliculas_pdf, name='peliculas_pdf'),

]