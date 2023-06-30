from django.shortcuts import render, redirect
from . import forms

def index(request):
    return render(request, "home/index.html",)

def crear_empleado(request):
    if request.method == "POST":
        form = forms.EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.EmpleadoForm()
    return render(request, "home/crear_empleado.html", {"form": form})
    
def crear_empleador(request):
    if request.method == "POST":
        form = forms.EmpleadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.EmpleadorForm()
    return render(request, "home/crear_empleador.html", {"form": form})
    
def crear_empleo(request):
    if request.method == "POST":
        form = forms.EmpleoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.EmpleoForm()
    return render(request, "home/crear_empleo.html", {"form": form})