from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("crear_empleado/", views.crear_empleado, name = "crear_empleado"),
    path("crear_empleador/", views.crear_empleador, name = "crear_empleador"),
    path("crear_empleo/", views.crear_empleo, name = "crear_empresa"),
]
