from django import forms

class HumanoFormulario(forms.form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    creacion = forms.DateField(required=False)