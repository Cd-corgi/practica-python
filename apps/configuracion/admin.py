from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Departamentos)
admin.site.register(Municipios)
admin.site.register(Terceros)
admin.site.register(FormaPago)
admin.site.register(Impuestos)
admin.site.register(Retenciones)
admin.site.register(VendedoresClientes)
admin.site.register(RetencionesClientes)
admin.site.register(RetencionesProveedor)
admin.site.register(PlazosDecuentosClientes)
admin.site.register(PlazosDecuentosProveedores)
admin.site.register(numeracion)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    '''Admin View for Empresa'''

    list_display = (
        'id', 
        'logo', 
        'slogan', 
        'razon_social', 
        'correo', 
        'departamento', 
        'municipio', 
        'nit', 
        'dv', 
        'actividadEconomica', 
        'nombreComercial', 
        'tipoPersona', 
        'obligaciones', 
        'telefono', 
        'registroMercantil', 
        'correoContacto', 
        'fecha_creacion', 
        'fecha_modificacion', 
        'estado', 
    )
    list_filter = ('razon_social',)
    search_fields = ('razon_social',)
    ordering = ('id',)




# @admin.register(DatosFacturacionElectronica)
# class DatosFacturacionElectronicaAdmin(admin.ModelAdmin):
#     '''Admin View for DatosFacturacionElectronica'''

#     exclude = ('__all__',)
#     list_filter = ('nombreComercial',)
    
    