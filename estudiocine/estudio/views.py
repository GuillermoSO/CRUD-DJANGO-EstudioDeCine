from django.shortcuts import render, redirect
from .models import Director
from .forms import DirectorForm
from .models import Guionista
from .forms import GuionistaForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

# DIRECTORES
def directores(request):
    directores = Director.objects.all()

    return render(request, 'directores/index.html', {'directores': directores})

def crear_director(request):
    formulario = DirectorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('directores')

    return render(request, 'directores/crear.html', {'formulario': formulario})

def editar_director(request, id):
    director = Director.objects.get(id=id)
    formulario = DirectorForm(request.POST or None, request.FILES or None, instance=director)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('directores')

    return render(request, 'directores/editar.html', {'formulario': formulario})

def eliminar_director(request, id):
    director = Director.objects.get(id=id)
    director.delete()
    return redirect('directores')

# GUIONISTAS
def guionistas(request):
    guionistas = Guionista.objects.all()

    return render(request, 'guionistas/index.html', {'guionistas': guionistas})

def crear_guionista(request):
    formulario = GuionistaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('guionistas')

    return render(request, 'guionistas/crear.html', {'formulario': formulario})

def editar_guionista(request, id):
    guionista = Guionista.objects.get(id=id)
    formulario = GuionistaForm(request.POST or None, request.FILES or None, instance=guionista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('guionistas')

    return render(request, 'guionistas/editar.html', {'formulario': formulario})

def eliminar_guionista(request, id):
    guionista = Guionista.objects.get(id=id)
    guionista.delete()
    return redirect('guionistas')
