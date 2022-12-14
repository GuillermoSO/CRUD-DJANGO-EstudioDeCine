from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from .models import Director
from .forms import DirectorForm
from .models import Guionista
from .forms import GuionistaForm
from .models import Pelicula
from .forms import PeliculaForm

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

# PELICULAS
def peliculas(request):
    peliculas = Pelicula.objects.all()

    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def crear_pelicula(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')

    return render(request, 'peliculas/crear.html', {'formulario': formulario})

def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')

    return render(request, 'peliculas/editar.html', {'formulario': formulario})

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas')

# REPORTES
# PELICULAS
def peliculas_pdf(request):
    # Bytestream buffer
    buf = io.BytesIO()
    # Canvas
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    # Text Object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    pelis = Pelicula.objects.all()  

    # CREO UNA LISTA EN BLANCO
    lines = ["LISTADO DE PELICULAS",
    " "
    ]

    for peli in pelis:
        lines.append("TITULO")
        lines.append(peli.Nombre)
        lines.append("DIRECTOR")
        lines.append(peli.Director.Nombre)
        lines.append("GUIONISTA")
        lines.append(peli.Guionista.Nombre)
        lines.append("------------------------------------")
       
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='peliculas.pdf')
