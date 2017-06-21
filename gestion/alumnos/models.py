from django.db import models

# Create your models here.

class Alumno(models.Model):
    dni             =       models.CharField(max_length=11)
    nombre          =       models.CharField(max_length=40)
    apellidos       =       models.CharField(max_length=100)
    class Meta:
        ordering = ["apellidos","nombre"]
    def __str__(self):
        return self.apellidos + " " + self.nombre
    
class Modulo(models.Model):
    codigo_junta    =       models.IntegerField(primary_key=True)
    nombre          =       models.CharField(max_length=120)
    def __str__(self):
        return self.nombre
    
class Tema(models.Model):
    nombre          =       models.CharField(max_length=60)
    numero          =       models.IntegerField()
    modulo          =       models.ForeignKey(Modulo)
    adicional       =       models.CharField(max_length=4096)
    class Meta:
        ordering = ["modulo__nombre", "numero"]
    def __str__(self):
        cad         =       "Tema " + str(self.numero) + " - " + self.nombre + " ("+str(self.modulo)+")"
        return cad
class AlumnoCursaModulo(models.Model):
    alumno          =       models.ForeignKey(Alumno)
    modulo          =       models.ForeignKey(Modulo)
    repite_modulo   =       models.BooleanField()
    class Meta:
        verbose_name_plural = "AlumnosCursanModulo"
    
class Examen(models.Model):
    nombre      =           models.CharField(max_length=90)
    tema        =           models.ForeignKey(Tema)
    def __str__(self):
        return str(self.nombre) + " - " + str(self.tema)
    class Meta:
        verbose_name_plural = "Examenes"
    
class AlumnoRealizaExamen(models.Model):
    alumno      =           models.ForeignKey(Alumno, related_name="AlumnoExamen")
    examen      =           models.ForeignKey(Examen)
    nota        =           models.DecimalField(max_digits=6, decimal_places=4)
    
    def __str__(self):
        cad=str(self.alumno) + " - " + str(self.examen) + " - Nota:"+str(self.nota)
        return cad
    class Meta:
        verbose_name_plural = "AlumnosRealizanExamen"
        ordering = ["alumno__apellidos"]