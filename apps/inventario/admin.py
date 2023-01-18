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



@admin.register(ProductosSumi)
class productosAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('nombreymarcaunico',)
    list_filter = ('nombreymarcaunico',)
    search_fields = ('nombreymarcaunico',)


@admin.register(Kardexs)
class KardexAdmin(admin.ModelAdmin):
    '''Admin View for productos'''

    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('descripcion',)
    

# @admin.register(OrdenDeCompra)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('id',)
#     list_filter = ('id',)


# @admin.register(OrdenDeCompraDetalle)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('id',)
#     list_filter = ('id',)


# @admin.register(Bodega)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('nombre',)
#     list_filter = ('nombre',)

# @admin.register(Marca)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('nombre',)
#     list_filter = ('nombre',)

# @admin.register(Unidad)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('nombre',)
#     list_filter = ('nombre',)

# @admin.register(Productos)
# class ProductosAdmin(admin.ModelAdmin):
#     '''Admin View for Productos'''

#     list_display = ('nombre','marca',)
#     list_filter = ('nombre','codigoDeBarra')
 