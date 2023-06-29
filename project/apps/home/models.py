from django.db import models

class user_empleado(models.Model):
    nombre = models.CharField(max_length = 30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


class user_empresa(models.Model):
    nombre = models.CharField(max_length = 30)
    edad = models.IntegerField()

class empleo(models.Model):
    empleo = models.CharField(max_length = 150)
    empresa = models.CharField(max_length = 50)
    sueldo = models.IntegerField()
