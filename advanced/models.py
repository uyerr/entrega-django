from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacimiento = models.DateField()