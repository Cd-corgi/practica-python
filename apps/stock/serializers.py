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

