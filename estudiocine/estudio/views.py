from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def directores(request):
    return render(request, 'directores/index.html')
def crear_director(request):
        return render(request, 'directores/crear.html')
def editar_director(request):
        return render(request, 'directores/editar.html')