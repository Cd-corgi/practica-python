from rest_framework import serializers
from django.db import transaction
<<<<<<< HEAD
=======
from .validations import *
>>>>>>> f58513177a9f48b4b59f095052d32872319ad21c
# from .validations import validarCliente,validarProveedor
from .models import *
# from apps.configuracion.models import puc

# from .serializers import TercerosCreateSerializer


<<<<<<< HEAD

=======
def registrar_OrdenDeCompra(create, orden, ordenDetalle):
        orden = OrdenDeCompra()
        if create:
                ValidarOrden(orden)

                num = numeracion.objects.get(id = orden['numeracion'])
                terceros = Terceros.objects.get(id = orden['proveedor'])
                formaPagos = FormaPago.objects.get(id = orden['formaPago'])
                persona = User.objects.get(username = orden['usuario'])

                orden.numeracion        = num
                orden.proveedor         = terceros
                orden.fecha             = orden['fecha']
                orden.usuario           = persona
                orden.formaPago         = formaPagos
                orden.subtotal          = orden['subtotal']
                orden.iva               = orden['iva']
                orden.retencion         = orden['retencion']
                orden.descuento         = orden['descuento']
                orden.total             = orden['total']

                with transaction.atomic():
                        orden.save()
                        detalle = []
                        for item in ordenDetalle:
                                d = OrdenDetalle()

                                p = item['producto']
                                prod = Productos.object.get(id = p.id)
                                d.orden       = orden
                                d.producto    = prod
                                d.cantidad    = item['cantidad']
                                d.valorUnidad = item['valorUnidad']   
                                if item['descuento'] == None or item['descuento'] == '':
                                        d.descuento   = item['descuento']
                                if item['iva'] == None or item['iva'] == '':
                                        d.iva   = item['iva']
                                detalle.append(d)
                        OrdenDetalle.objects.bulk_create(detalle)
                return orden
>>>>>>> f58513177a9f48b4b59f095052d32872319ad21c



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



   