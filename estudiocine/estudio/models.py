from unittest.util import _MAX_LENGTH
from django.db import models

# DIRECTOR
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name = 'Nombre')

    def __str__(self):
        return str(self.Nombre)

# GUIONISTA
class Guionista(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name = 'Nombre')

    def __str__(self):
        return str(self.Nombre)

# PELICULA
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name= 'Nombre')

    Director = models.ForeignKey(Director, on_delete=models.CASCADE, default=1, verbose_name= 'Director') 
    Guionista = models.ForeignKey(Guionista, on_delete=models.CASCADE, default=1, verbose_name= 'Guionista') 

    def __str__(self):
        return self.Nombre
