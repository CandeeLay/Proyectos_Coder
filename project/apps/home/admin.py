from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.user_empleado)
admin.site.register(models.user_empresa)
admin.site.register(models.empleo)