from django import forms

from . import models

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = models.crear_empleado
        fields = "__all__"

class EmpleadorForm(forms.ModelForm):
    class Meta:
        model = models.crear_empresa
        fields = "__all__"

class EmpleoForm(forms.ModelForm):
    class Meta:
        model = models.empleo
        fields = "__all__"
