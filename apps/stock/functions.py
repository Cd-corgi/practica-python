from rest_framework import serializers
from django.db import transaction
# from .validations import validarCliente,validarProveedor
from .models import *
# from apps.configuracion.models import puc

# from .serializers import TercerosCreateSerializer






def getProductos_SinStock():
        return Productos.objects.all().exclude(bodega=3).select_related('tipoProducto','bodega') 
    
def getProductosVentas():
        return Productos.objects.filter(stock_inicial__gt = 0).exclude(bodega=3).select_related('tipoProducto','bodega','impuesto')


def getProductosConsumo__SinStock():
        return Productos.objects.filter(bodega = 3).select_related('tipoProducto','bodega') 


def getProductosConsumoStock():
        return Productos.objects.filter(bodega = 3,stock_inicial__gt = 0).select_related('tipoProducto','bodega') 


def getKardex(idproducto):
    return Kardex.objects.filter(producto=idproducto).select_related('producto','tercero','bodega')


def getInventario(idproducto):
    return Inventario.objects.filter(idProducto=idproducto).select_related('idProducto','bodega').order_by('-vencimiento')



   