from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'