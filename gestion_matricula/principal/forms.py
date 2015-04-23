#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from principal.models import *
from users.models import *

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor


