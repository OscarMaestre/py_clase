from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Examen)
admin.site.register(AlumnoRealizaExamen)
admin.site.register(Modulo)
admin.site.register(AlumnoCursaModulo)
admin.site.register(Tema)