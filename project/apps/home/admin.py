from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.crear_empleado)
admin.site.register(models.crear_empresa)
admin.site.register(models.empleo)