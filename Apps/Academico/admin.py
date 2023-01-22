from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    '''Admin View for Curso'''

    list_display = (
        'id',
        'area',
        'creditos',
        'docente'
        )
    list_filter = ('area',)
    search_fields = (
        'id',
        'area',
        'creditos',
        'docente'
    )
    ordering = ('id',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    '''Admin View for Profesor'''

    list_display = (
        'id',
        'tipoDocumento',
        'documento',
        'nombreCompleto',
    )
    list_filter = ('tipoDocumento',)
    search_fields = (
        'id',
        'tipoDocumento',
        'documento',
        'nombreCompleto',
    )
    ordering = ('id',)