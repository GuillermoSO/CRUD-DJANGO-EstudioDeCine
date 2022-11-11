from django.contrib import admin
from .models import Director
from .models import Guionista
from .models import Pelicula

# Register your models here.
admin.site.register(Director)
admin.site.register(Guionista)
admin.site.register(Pelicula)