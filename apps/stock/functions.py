from rest_framework import serializers
from django.db import transaction

from .validations import *
from datetime import datetime
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
                tercero    = Terceros.objects.get(id = orden['proveedor'])
                formaPago  = FormaPago.objects.get(id = orden['formaPago'])
                usuario    = User.objects.get(id = orden['usuario'])

                # Asugnación de variables en general
                ordenNew.numeracion        = num
                ordenNew.consecutivo       = num.proximaFactura
                ordenNew.prefijo           = num.prefijo
                ordenNew.numero            = num.prefijo+'-'+str(num.proximaFactura)
                ordenNew.proveedor         = tercero
                ordenNew.fecha             = orden['fecha']
                ordenNew.usuario           = usuario
                ordenNew.formaPago         = formaPago
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
                                p             = item['producto']
                                prod          = Productos.objects.get(id = p['id'])
                                
                                # DETALLE 
                                d             = OrdenDetalle()
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
                        num.proximaFactura += 1
                        num.save()
                return ordenNew
        else:
                # Consulta de la ID del modelo de OrdenDetalle con OrdenDeCompra
                try:
                     ordenNew = OrdenDeCompra.objects.get(id = orden['id'])
                except ordenNew.ObjectDoesNotExist as e:
                        raise serializers.ValidationError('La id por actualizar no existe')
                
                # Asignación de variables de las Foreign Keys
                num       = numeracion.objects.get(id = orden['numeracion'])
                tercero   = Terceros.objects.get(id = orden['proveedor'])
                formaPago = FormaPago.objects.get(id = orden['formaPago'])
                usuario   = User.objects.get(id = orden['usuario'])

                # Asugnación de variables en general
                ordenNew.numeracion        = num
                ordenNew.proveedor         = tercero
                ordenNew.fecha             = orden['fecha']
                ordenNew.usuario           = usuario
                ordenNew.formaPago         = formaPago
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
                                prod          = Productos.objects.get(id = p['id'])

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
                        num.proximaFactura += 1
                        num.save()
                return ordenNew

def ListOrdenCompra():
        return  OrdenDeCompra.objects.all().select_related(
        'numeracion',
        'proveedor',
        'formaPago',
        'usuario'
        ).order_by('-fecha')

def GetOrdenCompra(id):
        return  OrdenDeCompra.objects.select_related(
                'numeracion',
                'proveedor',
                'formaPago',
                'usuario'
                ).prefetch_related(
                'detalle_orden'
                ).get(id = id)

                  
def registrar_Ingreso(create, ingreso, ingresoDetalle):
        NewIngreso = Ingreso()
        ValidarIngreso(ingreso)
        if create:
                # Llamando datos de otras tablas
                num     = numeracion.objects.get(id = ingreso['numeracion'])
                orden   = OrdenDeCompra.objects.get(id = ingreso['orden'])
                usuario = User.objects.get(id = ingreso['usuario'])

                # Asignando datos
                NewIngreso.numeracion        = num
                NewIngreso.consecutivo       = num.proximaFactura
                NewIngreso.prefijo           = num.prefijo
                NewIngreso.numero            = num.prefijo+'-'+str(num.proximaFactura)
                NewIngreso.factura           = ingreso['factura']
                NewIngreso.orden             = orden
                NewIngreso.proveedor         = orden.proveedor
                NewIngreso.fecha             = ingreso['fecha']
                NewIngreso.formaPago         = orden.formaPago
                NewIngreso.usuario           = usuario
                NewIngreso.subtotal          = ingreso['subtotal']
                NewIngreso.iva               = ingreso['iva']
                NewIngreso.retencion         = ingreso['retencion']
                NewIngreso.descuento         = ingreso['descuento']
                NewIngreso.total             = ingreso['total']

                # Creando datos para Cuentas x Pagar Compras 
                CuentaxP = CxPCompras()

                # Recopilando Datos
                CuentaxP.proveedor  = NewIngreso.proveedor
                CuentaxP.base       = NewIngreso.subtotal
                CuentaxP.iva        = NewIngreso.iva
                CuentaxP.reteFuente = NewIngreso.retencion  
                CuentaxP.total      = NewIngreso.total  


                # CuentaxP.reteIca    = NewIngreso.retencion 



                with transaction.atomic():
                        # Se guardan los datos
                        NewIngreso.save()

                        # Obteniendo el ingreso de la consulta anterior (ingreso)
                        CuentaxP.ingreso = NewIngreso

                        # Guarda los datos 
                        CuentaxP.save()

                        detalle = []
                        for item in ingresoDetalle:
                                # Inicializa las variables para poder agregar productos y kardex
                                p                  = item['producto']
                                d                  = IngresoDetalle()    
                                k                  = Kardex()

                                # Obtiene los datos del producto a agregar
                                product            = Productos.objects.get(id = p['id'])

                                # Añadiendo los datos de IngresoDetalle
                                d.ingreso          = NewIngreso
                                d.producto         = product
                                d.cantidad         = item['cantidad']
                                d.valorUnidad      = item['valorUnidad']
                                d.lote             = item['lote']
                                d.laboratorio      = item['laboratorio']
                                d.fechaVencimiento = item['fechaVencimiento']

                                # Si el iva y descuento de ingreso detalle están vacios o nulos
                                if item['iva'] == None or item['iva'] == '':
                                        d.iva       = 0
                                else :
                                        d.iva = item['iva']                                        
                                if item['descuento'] == None or item['descuento'] == '':
                                        d.descuento = 0
                                else:
                                        d.descuento = item['descuento']

                                # Guarda los datos de ingreeso Detalle
                                d.save()

                                # Ahora se llama los datos del kardex a registrar
                                k.descripcion = 'Ingreso No. '+d.ingreso.numero
                                k.tipo        = 'IN'
                                k.producto    = d.producto
                                k.tercero     = d.ingreso.proveedor
                                k.bodega      = d.producto.bodega
                                k.unidades    = d.cantidad
                                k.balance     = d.producto.stock_inicial + d.cantidad
                                k.precio      = d.valorUnidad

                                # Guarda los kardex de los productos
                                k.save()

                                # validando el inventario
                                if Inventario.objects.filter(idProducto = d.producto.id,lote = d.lote,laboratorio = d.laboratorio).exist():
                                        producto          = Inventario.objects.get(idProducto = d.producto.id,lote = d.lote,laboratorio = d.laboratorio)
                                        producto.unidades +=  d.cantidad
                                        producto.save()

                                        # actualizando Producto
                                        product.stock_inicial += d.cantidad
                                        
                                        product.save()


                                else:
                                        # Registra nuevo producto en el inventario
                                        newProductInv = Inventario()

                                        # Se agisnan los datos
                                        newProductInv.bodega      = d.producto.bodega
                                        newProductInv.idProducto  = d.producto.id
                                        newProductInv.vencimiento = d.fechaVencimiento
                                        newProductInv.valorCompra = d.valorUnidad
                                        newProductInv.unidades    = d.cantidad
                                        newProductInv.lote        = d.lote
                                        newProductInv.estado      = True                                             
                                        newProductInv.laboratorio = d.laboratorio

                                        # Guarda los datos
                                        newProductInv.save()

                        num.proximaFactura += 1
                        num.save()
      

                       
                  
                                



                return NewIngreso
        else:
                try:
                        NewIngreso = Ingreso.objects.get(id = ingreso['id'])
                except NewIngreso.ObjectDoesNotExist as e:
                        raise serializers.ValidationError("La id por actualizar no existe")

                # Llamando datos de otras tablas
                num     = numeracion.objects.get(id = ingreso['numeracion'])
                orden   = OrdenDeCompra.objects.get(id = ingreso['orden'])
                usuario = User.objects.get(id = ingreso['usuario'])

                # Asignando datos
                NewIngreso.numeracion        = num
                NewIngreso.consecutivo       = num.proximaFactura
                NewIngreso.prefijo           = num.prefijo
                NewIngreso.numero            = num.prefijo+'-'+str(num.proximaFactura)
                NewIngreso.factura           = ingreso['factura']
                NewIngreso.orden             = orden
                NewIngreso.proveedor         = orden.proveedor
                NewIngreso.fecha             = ingreso['fecha']
                NewIngreso.formaPago         = orden.formaPago
                NewIngreso.usuario           = usuario
                NewIngreso.subtotal          = ingreso['subtotal']
                NewIngreso.iva               = ingreso['iva']
                NewIngreso.retencion         = ingreso['retencion']
                NewIngreso.descuento         = ingreso['descuento']
                NewIngreso.total             = ingreso['total']


                with transaction.atomic():
                        NewIngreso.save()
                        IngresoD = IngresoDetalle.objects.get(id = ingreso['id'])
                        IngresoD.delete()
                        for item in ingresoDetalle:
                                p                  = item['producto']
                                product            = Productos.objects.get(id = p['id'])

                                d                  = IngresoDetalle()
                                d.ingreso          = NewIngreso
                                d.producto         = product
                                d.cantidad         = item['cantidad']
                                d.valorUnidad      = item['valorUnidad']
                                if item['iva'] == None or item['iva'] == '':
                                        d.iva       = 0
                                else :
                                        d.iva = item['iva']                                        
                                if item['descuento'] == None or item['descuento'] == '':
                                        d.descuento = 0
                                else:
                                        d.descuento = item['descuento']
                                detalle.append(d)
                        IngresoDetalle.objects.bulk_create(detalle)
                return NewIngreso                                                



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

