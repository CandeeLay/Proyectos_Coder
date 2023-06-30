from django.db import models

class crear_empleado(models.Model):
    nombre = models.CharField(max_length = 30)
    edad = models.IntegerField()
    experiencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class crear_empresa(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length = 50, blank=True, null=True) 

class empleo(models.Model):
    empleo = models.CharField(max_length = 150)
    sueldo = models.IntegerField()
    empresa = models.CharField(max_length = 30)