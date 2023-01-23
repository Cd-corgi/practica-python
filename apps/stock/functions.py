from rest_framework import serializers
from django.db import transaction

from .validations import *

# from .validations import validarCliente,validarProveedor
from .models import *
# from apps.configuracion.models import puc

# from .serializers import TercerosCreateSerializer


def registrar_OrdenDeCompra(create, orden, ordenDetalle):
        ordenNew = OrdenDeCompra()
        ValidarOrden(orden)
        if create:
                # Asignación de variables de las Foreign Keys
                num        = numeracion.objects.get(id = orden['numeracion'])
                terceros   = Terceros.objects.get(id = orden['proveedor'])
                formaPagos = FormaPago.objects.get(id = orden['formaPago'])
                persona    = User.objects.get(username = orden['usuario'])

                # Asugnación de variables en general
                ordenNew.numeracion        = num
                ordenNew.proveedor         = terceros
                ordenNew.fecha             = orden['fecha']
                ordenNew.usuario           = persona
                ordenNew.formaPago         = formaPagos
                ordenNew.subtotal          = orden['subtotal']
                ordenNew.iva               = orden['iva']
                ordenNew.retencion         = orden['retencion']
                ordenNew.descuento         = orden['descuento']
                ordenNew.total             = orden['total']

                # Atomic que procesa los cambios y añade mas valoes a OrdenDetalle
                with transaction.atomic():
                        ordenNew.save()
                        detalle = []
                        # for que itera todo los campos de OrdenDetalle
                        for item in ordenDetalle:
                                d             = OrdenDetalle()
                                p             = item['producto']
                                prod          = Productos.object.get(id = p.id)
                                d.orden       = ordenNew
                                d.producto    = prod
                                d.cantidad    = item['cantidad']
                                d.valorUnidad = item['valorUnidad']   
                                if item['descuento'] == None or item['descuento'] == '':
                                        d.descuento   = item['descuento']
                                if item['iva'] == None or item['iva'] == '':
                                        d.iva   = item['iva']
                                # Añade los datos al arreglo "Detalle"
                                detalle.append(d)
                        # Hace una inserción masiva a OrdenDetalle                                
                        OrdenDetalle.objects.bulk_create(detalle)
                return ordenNew
        else:
                # Consulta de la ID del modelo de OrdenDetalle con OrdenDeCompra
                try:
                     ordenNew = OrdenDeCompra.objects.get(id = orden['id'])
                except ordenNew.ObjectDoesNotExist as e:
                        raise serializers.ValidationError('La id por actualizar no existe')
                
                # Asignación de variables de las Foreign Keys
                num        = numeracion.objects.get(id = orden['numeracion'])
                terceros   = Terceros.objects.get(id = orden['proveedor'])
                formaPagos = FormaPago.objects.get(id = orden['formaPago'])
                persona    = User.objects.get(username = orden['usuario'])

                # Asugnación de variables en general
                ordenNew.numeracion        = num
                ordenNew.proveedor         = terceros
                ordenNew.fecha             = orden['fecha']
                ordenNew.usuario           = persona
                ordenNew.formaPago         = formaPagos
                ordenNew.subtotal          = orden['subtotal']
                ordenNew.iva               = orden['iva']
                ordenNew.retencion         = orden['retencion']
                ordenNew.descuento         = orden['descuento']
                ordenNew.total             = orden['total']

                # Atomic que procesa los cambios y añade mas valoes a OrdenDetalle
                with transaction.atomic():
                        ordenNew.save()
                        ordenD = OrdenDetalle.objects.filter(orden = orden['id'])
                        ordenD.delete()
                        detalle = []
                        # for que itera todo los campos de OrdenDetalle
                        for item in ordenDetalle:
                                d             = OrdenDetalle()
                                p             = item['producto']
                                prod          = Productos.object.get(id = p.id)
                                d.orden       = ordenNew
                                d.producto    = prod
                                d.cantidad    = item['cantidad']
                                d.valorUnidad = item['valorUnidad']   
                                if item['descuento'] == None or item['descuento'] == '':
                                   d.descuento   = 0
                                else: 
                                   d.descuento   = item['descuento']   
                                if item['iva'] == None or item['iva'] == '':
                                   d.iva   = 0
                                else:
                                   d.iva   = item['iva']
                                # Añade los datos al arreglo "Detalle"
                                detalle.append(d)
                        # Hace una inserción masiva a OrdenDetalle        
                        OrdenDetalle.objects.bulk_create(detalle)
                return ordenNew

                


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



   