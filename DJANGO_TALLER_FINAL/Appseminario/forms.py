from dataclasses import fields
from socket import fromshare
from django import forms
from Appseminario.models import Inscripcion

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'

    fecha_inscripcion = forms.DateField(label="Fecha de la inscripción", widget=forms.SelectDateWidget)
    hora_inscripcion = forms.TimeField(label="Hora de la inscripción", widget=forms.TimeInput(attrs={'type':'time'}))