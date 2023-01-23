from rest_framework import serializers
# from apps.users.serializers import UserListSerializers 

from .models import (
    Departamentos,
    Municipios,
    Empresa,
    Impuestos,
    Retenciones,
    PlazosDecuentosClientes,
    PlazosDecuentosProveedores,
    RetencionesClientes,
    RetencionesProveedor,
    Terceros,
    FormaPago,
    VendedoresClientes,
    numeracion
)






class RetencionesClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model  = RetencionesClientes
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class RetencionesProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model  = RetencionesProveedor
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class PlazosDescuentosClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model  = PlazosDecuentosClientes
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class PlazosDescuentosProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PlazosDecuentosProveedores
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class VendedoresSerializer(serializers.ModelSerializer):

    class Meta:
        model  = VendedoresClientes
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response



class ImpuestosSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Impuestos
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class RetencionesSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Retenciones
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response





class MunicipiosCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Municipios
        fields = ('id','codigo','municipio')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["codigo"] = instance.codigo.replace(".", "")
        return response

class DepartamentosListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Departamentos
        fields = ('id','codigo','departamento')


    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["codigo"] = instance.codigo.replace(".", "")
        return response


class DepartamentosCreateSerializer(serializers.ModelSerializer):
    municipios = MunicipiosCreateSerializer(source="departamentos_municipios", many = True)
    class Meta:
        model  = Departamentos
        fields = ('id','codigo','departamento','municipios')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["codigo"] = instance.codigo.replace(".", "")
        return response




class EmpresaCreateSerializer(serializers.ModelSerializer):
    # datosFE = DatosFacturacionElectronicaCreateSerializer(source="empresa_datosFE")
    class Meta:
        model  = Empresa
        fields = ('logo','slogan','razon_social','correo','departamento','municipio','nit','telefono')


class EmpresaListSerializer(serializers.ModelSerializer):
    # datosFE = DatosFacturacionElectronicaCreateSerializer(source = "empresa_datosFE")
    departamento = DepartamentosCreateSerializer()
    municipio = MunicipiosCreateSerializer()
    class Meta:
        model  = Empresa
        fields = ('id','logo','slogan','razon_social','correo','departamento','municipio','nit','telefono')

    def to_representation(self, instance):
        
        response = super().to_representation(instance)
        return response

# class PlazosDescuentosCreateSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model  = PlazosDecuentos
#         fields = ('__all__')

class FormaPagoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model  = FormaPago
        fields = ('__all__')

    

class TercerosCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Terceros
        fields = ('__all__')


    def to_representation(self, instance):
        
        response = super().to_representation(instance)

        response['departamento'] = instance.departamento.departamento
        response['municipio'] = instance.municipio.municipio
        return response


class TercerosListSerializer(serializers.ModelSerializer):
    vendedor                 = VendedoresSerializer()
    # cuenta_x_cobrar          = pucSerializer()
    # cuenta_x_pagar           = pucSerializer()
    # cuenta_saldo_a_cliente   = pucSerializer()
    # cuenta_saldo_a_proveedor = pucSerializer()
    formaPago                = FormaPagoCreateSerializer()
    departamento             = DepartamentosListSerializer()
    municipio                = MunicipiosCreateSerializer()
    descuentoCliente         = PlazosDescuentosClientesSerializer(source = "plazos_clientes", many = True)
    descuentoProveedor       = PlazosDescuentosProveedorSerializer(source = "plazos_proveedores",many = True)
    retencionCliente         = RetencionesClientesSerializer(source      = "retencion_cliente", many = True)
    retencionProveedor       = RetencionesProveedorSerializer(source = "retencion_proveedor", many = True)

    class Meta:
        model  = Terceros
        fields = (
            'id',
            'tipoDocumento',
            'documento',
            'dv',
            'nombreComercial',
            'nombreContacto',
            'direccion',
            'departamento',
            'municipio',
            'telefonoContacto',
            'correoContacto',
            'correoFacturas',
            'vendedor',
            'formaPago',
            'tipoPersona',
            'regimen',
            'obligaciones',
            'matriculaMercantil',
            'codigoPostal',
            'saldoAFavorProveedor',
            'saldoAFavorCliente',
            'isCliente',
            'isProveedor',
            'isContabilidad',
            'isCompras',
            'isPos',
            'isElectronico',
            'cuenta_x_cobrar',
            'cuenta_x_pagar',
            'cuenta_saldo_a_cliente',
            'cuenta_saldo_a_proveedor',
            'montoCreditoProveedor',
            'montoCreditoClientes',
            'fecha_creacion',
            'fecha_modificacion',
            'estado',
            'descuentoCliente',
            'descuentoProveedor',
            'retencionCliente',
            'retencionProveedor'
        )


    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response



class VendedoresSerializer(serializers.ModelSerializer):

    class Meta:
        model  = VendedoresClientes
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

class NumeracionSerializer(serializers.ModelSerializer):

    class Meta:
        model  = numeracion
        fields = ('__all__')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response





