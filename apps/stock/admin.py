from django.contrib import admin

# Register your models here.
from .models import *



@admin.register(Bodega)
class bodegaAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)


@admin.register(tipoProducto)
class tipoProductoAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('vencimiento',)
    list_filter = ('vencimiento',)
    search_fields = ('vencimiento',)

@admin.register(Productos)
class productosAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('nombreymarcaunico',)
    list_filter = ('nombreymarcaunico',)
    search_fields = ('nombreymarcaunico',)


@admin.register(Kardex)
class KardexAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('descripcion',)