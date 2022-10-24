from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    especie = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
    
class BusquedaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)