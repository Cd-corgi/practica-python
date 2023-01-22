from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    cru = Curso.objects.all()
    pro = Profesor.objects.all()
    return render(request, "Cursos.html", { "cursos": cru, "profesor": pro })

def registrarCursos(request):
    if Curso.objects.filter(area = request.POST['txtArea']).exists():
        return redirect('/')
    else:
        area        = request.POST['txtArea']

    if request.POST['txtNumero'] == None or request.POST['txtNumero'] == '':
        creditos    = 0
    else:
        creditos    = request.POST['txtNumero']
    if Profesor.objects.filter(documento = request.POST['txtMenu']) is None or Profesor.objects.filter(documento = request.POST['txtMenu']) == "":
        return redirect('/')
    prof = Profesor.objects.get(documento = request.POST['txtMenu'])   
    docente = prof     
    curso = Curso.objects.create(area=area, creditos=creditos, docente = docente)   
    return redirect('/') 

def eliminarCursos(request, area):
    cc = Curso.objects.get(area = area)
    
    cc.delete()
    return redirect('/')

def edicionCursos(request, area):
    cc = Curso.objects.get(area = area)
    pro = Profesor.objects.all()
    return render(request, 'editarArea.html', {"cursos": cc, "profesor": pro})

def editarArea(request):
    id             = request.POST['txtIDE']
    area           = request.POST['txtAreaE']
    creditos       = request.POST['txtNumeroE']
    docente        = request.POST['txtMenuE']

    curso = Curso.objects.get(id = id)

    profe = Profesor.objects.get(documento = docente)
    print(profe.nombreCompleto)

    curso.area       = area
    if request.POST['txtNumeroE'] == None or request.POST['txtNumeroE'] == '':
        creditos    = 0
    curso.creditos   = creditos
    curso.docente    = profe
    curso.save()

    return redirect('/')       