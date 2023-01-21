from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    cru = Curso.objects.all()
    return render(request, "Cursos.html", { "cursos": cru })

def registrarCursos(request):
    if Curso.objects.filter(area = request.POST['txtArea']).exists():
        messages.success(request, 'El area a agregar ya existe')
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

    if Curso.objects.filter(area = cc) is None:
        return messages.warning(request, 'El dato a eliminar no existe')
    
    cc.delete()
    return redirect('/')