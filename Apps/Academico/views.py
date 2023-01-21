from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    cru = Curso.objects.all()
    return render(request, "Cursos.html", { "cursos": cru })

def registrarCursos(request):
    if Curso.objects.filter(area = request.POST['txtArea']).exists():
        return redirect('/')
    else:
        area        = request.POST['txtArea']

    if request.POST['txtNumero'] == None or request.POST['txtNumero'] == '':
        creditos    = 0
    else:
        creditos    = request.POST['txtNumero']  

    curso = Curso.objects.create(area=area, creditos=creditos)   
    return redirect('/') 

def eliminarCursos(request, area):
    cc = Curso.objects.get(area = area)
    
    cc.delete()
    return redirect('/')