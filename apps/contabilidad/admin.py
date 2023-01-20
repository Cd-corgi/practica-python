from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(asiento)
class AsientoAdmin(admin.ModelAdmin):
    '''Admin View of asiento'''
    list_display = (
        'id',
        'numero',
        'fecha',
        'mes',
        'anio',
        'empresa',
        'usuario',
        'totalDebito',
        'totalCredito'
    )
    list_filter = ('numero',)
    search_fields = (
        'id',
        'numero',
        'fecha',
        'mes',
        'anio',
        'empresa',
        'usuario',
        'totalDebito',
        'totalCredito'
    )
    ordering = ('id',)


@admin.register(asientoDetalle)
class AsientoDetalleAdmin(admin.ModelAdmin):
    '''Admin View of asientoDetalle'''
    list_display = (
        'id',
        'asiento',
        'tercero',
        'cuenta',
        'debito',
        'credito',
        'fecha',
        'mes',
        'anio'
    )
    list_filter = ('tercero',)
    search_fields = (
        'id',
        'asiento',
        'tercero',
        'cuenta',
        'debito',
        'credito',
        'fecha',
        'mes',
        'anio'
    )
    ordering = ('id',)


@admin.register(ComprobantesContable)
class ComprobantesContablesAdmin(admin.ModelAdmin):
    '''Admin View of ComprobantesContables'''
    list_display = (
        'id',
        'numeracion',
        'numero',
        'consecutivo',
        'referencia',
        'empresa',
        'usuario',
        'total',
        'observaciones',
        'fecha',
        'mes',
        'anio'
    )
    list_filter = ('numeracion',)
    search_fields = (
        'id',
        'numeracion',
        'numero',
        'consecutivo',
        'referencia',
        'empresa',
        'usuario',
        'total',
        'observaciones',
        'fecha',
        'mes',
        'anio'
    )
    ordering = ('id',)


@admin.register(CombrobantesDetalleContable)
class CombrobantesDetalleContableAdmin(admin.ModelAdmin):
    '''Admin View of CombrobanteDetalleContable'''
    list_display = (
        'id',
        'comprobante',
        'tercero',
        'cuenta',
        'descripcion',
        'debito',
        'credito',
        'fecha'
    )
    list_filter = ('tercero',)
    search_fields = (
        'id',
        'comprobante',
        'tercero',
        'cuenta',
        'descripcion',
        'debito',
        'credito',
        'fecha'
    )
    ordering = ('id',)


@admin.register(puc)
class pucAdmin(admin.ModelAdmin):
    '''Admin View of puc'''
    list_display = (
        'id',
        'tipoDeCuenta',
        'naturaleza',
        'nombre',
        'codigo',
        'estadoFinanciero',
        'estadoResultado',
        'padre'
    )
    list_filter = ('tipoDeCuenta',)
    search_fields = (
        'id',
        'tipoDeCuenta',
        'naturaleza',
        'nombre',
        'codigo',
        'estadoFinanciero',
        'estadoResultado',
        'padre'
    ),
    ordering = ('id', )
