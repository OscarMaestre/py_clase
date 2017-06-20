from django.db import models

# Create your models here.

class Alumno(models.Model):
    dni             = models.CharField(max_length=11)
    nombre          = models.CharField(max_length=40)
    apellidos       = models.CharField(max_length=100)
    
    
class Modulo(models.Model):
    codigo_junta    =   models.IntegerField(primary_key=True)
    nombre          =   models.CharField(max_length=120)
    
class AlumnoCursaModulo(models.Model):
    alumno          =       models.ForeignKey(Alumno)
    modulo          =       models.ForeignKey(Modulo)
    repite_modulo   =       models.BooleanField()