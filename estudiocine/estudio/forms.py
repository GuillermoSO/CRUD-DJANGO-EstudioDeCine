from attr import field, fields
from django import forms
from .models import Director
from .models import Guionista
from .models import Pelicula

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields ='__all__'

class GuionistaForm(forms.ModelForm):
    class Meta:
        model = Guionista
        fields ='__all__'

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields ='__all__'