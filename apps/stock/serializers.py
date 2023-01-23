from rest_framework import serializers
# from apps.users.serializers import UserListSerializers 

from apps.users.serializers import UserListSerializers
from apps.configuracion.serializers import *

from .models import *

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Bodega
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class tipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = tipoProducto
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response



class ProductosSerializer(serializers.ModelSerializer):
    tipoProducto = tipoProductoSerializer()
    bodega       = BodegaSerializer()
    impuesto     = ImpuestosSerializer()
    
    class Meta:
        model  = Productos
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response



class KardexSerializer(serializers.ModelSerializer):
    producto     = ProductosSerializer()
    bodega       = BodegaSerializer()
    tercero      = TercerosCreateSerializer()

    class Meta:
        model  = Kardex
        fields = ('__all__')


    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

    
class InventarioSerializer(serializers.ModelSerializer):
    idProducto     = ProductosSerializer()
    bodega         = BodegaSerializer()

    class Meta:
        model  = Inventario
        fields = ('__all__')


    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class OrdenDeCompraSerializer(serializers.ModelSerializer):
    numeracion  = NumeracionSerializer()
    proveedor   = TercerosCreateSerializer()
    formaPago   = FormaPagoCreateSerializer()

    class Meta:
        model = OrdenDeCompra
        fileds = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class OrdenDetalleSerializer(serializers.ModelSerializer):
    orden       = OrdenDeCompraSerializer()
    producto    = ProductosSerializer()

    class Meta:
        model   = OrdenDetalle
        fields  = ('__all__')   
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class ImpuestoOrdenSerializer(serializers.ModelSerializer):
    orden       = OrdenDeCompraSerializer()
    impuesto    = ImpuestosSerializer()

    class Meta:
        model = ImpuestoOrden
        fields = ('__all__')        

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class RetencionOrdenSerializer(serializers.ModelSerializer):
    orden       = OrdenDeCompraSerializer()
    retencion   = RetencionesSerializer() 
    
    class Meta:
        model = RetencionOrden
        fields = ('__all__')    

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class IngresoSerializer(serializers.ModelSerializer):
    numeracion    = NumeracionSerializer()
    orden         = OrdenDeCompraSerializer()
    proveedor     = TercerosCreateSerializer()
    formaPago     = FormaPagoCreateSerializer()
    ususario      = UserListSerializers()
    
    class Meta:
        model = Ingreso
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response        

class IngresoDetalleSerializer(serializers.ModelSerializer):
    ingreso     = IngresoSerializer()
    productos   = ProductosSerializer()

    class Meta:
        model = IngresoDetalle
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class ImpuestoIngresoSeriliazer(serializers.ModelSerializer):
    ingreso     = IngresoSerializer()
    impuesto    = ImpuestosSerializer()
    
    class Meta:
        model = ImpuestoIngreso
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class RetencionIngresoSerializer(serializers.ModelSerializer):
    ingreso     = IngresoSerializer()
    retencion   = RetencionesSerializer()
    
    class Meta:
        model = RetencionIngreso
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class CxPComprasSerializer(serializers.ModelSerializer):
    ingreso     = IngresoSerializer()
    formaPago   = FormaPagoCreateSerializer()
    proveedor   = TercerosCreateSerializer()

    class Meta:
        model = CxPCompras
        fields = ('__all__')
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class PagosComprasSerializer(serializers.ModelSerializer):
    numeracion  = NumeracionSerializer()
    ingreso     = IngresoSerializer()
    usuario     = UserListSerializers()

    class Meta:
        model = PagosCompras
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class NotaDebitoSerializer(serializers.ModelSerializer):
    numeracion  = NumeracionSerializer()
    ingreso     = IngresoSerializer()
    proveedor   = TercerosCreateSerializer()
    usuario     = UserListSerializers()
    
    class Meta:
        model = NotaDebito
        filds = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class NotaDebitoDetalleSerializer(serializers.ModelSerializer):
    nota        = NotaDebitoSerializer()
    producto    = ProductosSerializer()

    class Meta:
        module = NotaDebitoDetalle
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class NotaCreditoSerializer(serializers.ModelSerializer):
    numeracion  = NumeracionSerializer()
    ingreso     = IngresoSerializer()
    proveedor   = TercerosCreateSerializer()

    class Meta:
        module = NotaCredito
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response        

class DetalleNotaCreditoSerializer(serializers.ModelSerializer):
    nota        = NotaCreditoSerializer()
    producto    = ProductosSerializer()
    
    class Meta:
        module = DetalleNotaCredito
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response