from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name = 'Nombre')

    def __str__(self) -> str:
        fila = "Nombre: " + self.Nombre 
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()
