from attr import field, fields
from django import forms
from .models import Director
from .models import Guionista

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields ='__all__'

class GuionistaForm(forms.ModelForm):
    class Meta:
        model = Guionista
        fields ='__all__'