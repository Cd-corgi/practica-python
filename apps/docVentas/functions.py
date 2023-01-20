from rest_framework import serializers
from django.db import transaction
from .validations import validarCliente,validarProveedor
from .models import *
from apps.configuracion.models import puc

from .serializers import TercerosCreateSerializer

def saveTercero(create,tercero,descuentoCliente,descuentoProveedor,retencionesClientes,retencionesProveedor):
    if create:
        if Terceros.objects.filter(documento=tercero['documento']).exists():
            raise serializers.ValidationError('Ya existe un tercero con este documento.')
    if tercero['isCliente']:
        validarCliente(tercero)
    if tercero['isProveedor']:
        validarProveedor(tercero)

    t            = None
    descuentoC   = None  
    descuentoP   = None
    retencionesC = None
    retencionesP = None
    id = 0
    if tercero['id']:
        id = tercero['id']
    if Terceros.objects.filter(id=id).exists():
        t            = Terceros.objects.get(id=tercero['id'])
        descuentoC   = PlazosDecuentosClientes.objects.get(id=descuentoCliente['id']).delete()
        descuentoP   = PlazosDecuentosProveedores.objects.get(id=descuentoProveedor['id']).delete()
        retencionesC = RetencionesClientes.objects.filter(tercero=t.id).delete()
        retencionesP = RetencionesProveedor.objects.filter(tercero=t.id).delete()
    else:
        t            = Terceros()
        descuentoC   = PlazosDecuentosClientes()  
        descuentoP   = PlazosDecuentosProveedores()
        retencionesC = RetencionesClientes()
        retencionesP = RetencionesProveedor()
    

    departamento     = Departamentos.objects.get(id = tercero['departamento'])
    municipio        = Municipios.objects.get(id = tercero['municipio'])
    formaDePago      = FormaPago.objects.get(id = tercero['formaPago'])

    
    t.tipoDocumento            = tercero['tipoDocumento']
    t.documento                = tercero['documento']
    t.dv                       = tercero['dv']
    t.nombreComercial          = tercero['nombreComercial']
    t.nombreContacto           = tercero['nombreContacto']
    t.direccion                = tercero['direccion']
    t.departamento             = departamento
    t.municipio                = municipio
    t.telefonoContacto         = tercero['telefonoContacto']
    t.correoContacto           = tercero['correoContacto']
    t.correoFacturas           = tercero['correoFacturas']

    if tercero['isCliente']:
        vendedor = VendedoresClientes.objects.get(id = tercero['vendedor'])
        c_cobrar = puc.objects.get(id = tercero['cuenta_x_cobrar'])
        c_saldo  = puc.objects.get(id = tercero['cuenta_saldo_a_cliente'])

        t.vendedor  = vendedor
        t.cuenta_x_cobrar        = c_cobrar
        t.cuenta_saldo_a_cliente = c_saldo 
    
    t.formaPago                = formaDePago
    t.tipoPersona              = tercero['tipoPersona']
    t.regimen                  = tercero['regimen']
    t.matriculaMercantil       = tercero['matriculaMercantil']
    t.codigoPostal             = tercero['codigoPostal']
    t.isCliente                = tercero['isCliente']
    t.isProveedor              = tercero['isProveedor']
    t.isCompras                = tercero['isCompras']
    t.isContabilidad           = tercero['isContabilidad']
    t.isElectronico            = tercero['isElectronico']
    t.isPos                     = tercero['isPos']

    if tercero['isProveedor']:
        p_pagar  = puc.objects.get(id = tercero['cuenta_x_pagar'])
        p_saldo  = puc.objects.get(id = tercero['cuenta_saldo_a_proveedor'])

        t.cuenta_x_pagar           = p_pagar  
        t.cuenta_saldo_a_proveedor = p_saldo  
        
    with transaction.atomic():
        t.save()

        if descuentoCliente:
            descuentoC.tercero        = t
            descuentoC.quince         = descuentoCliente['quince']
            descuentoC.treinta        = descuentoCliente['treinta']
            descuentoC.cuarentaYcinco = descuentoCliente['cuarentaycinco']
            descuentoC.sesenta        = descuentoCliente['sesenta']
            descuentoC.noventa        = descuentoCliente['noventa']
            descuentoC.save()
        
        if descuentoProveedor: 
            descuentoP.tercero        = t
            descuentoP.quince         = descuentoProveedor['quince']
            descuentoP.treinta        = descuentoProveedor['treinta']
            descuentoP.cuarentaYcinco = descuentoProveedor['cuarentaycinco']
            descuentoP.sesenta        = descuentoProveedor['sesenta']
            descuentoP.noventa        = descuentoProveedor['noventa']
            descuentoP.save()
        
        if retencionesClientes:

            lista = []
            for x in retencionesClientes:
                j = x['retencion']
                r = Retenciones.objects.get(id = j['id']) 
                RTF = RetencionesClientes(
                    tercero   = t,
                    retencion = r,
                    fija      = x['fija']
                )
                RTF.save()
        if retencionesProveedor:
            lista = []
            for x in retencionesProveedor:
                j = x['retencion']
                r = Retenciones.objects.get(id = j['id']) 
                RTF = RetencionesProveedor(
                    tercero   = t,
                    retencion = r,
                    fija      = x['fija']
                )
                RTF.save()
    return t



def getTerceros(tipo):
    if tipo == 'TODOS':
        return Terceros.objects.all().select_related('vendedor','cuenta_x_cobrar','cuenta_x_pagar','cuenta_saldo_a_cliente','cuenta_saldo_a_proveedor','formaPago','departamento','municipio').prefetch_related('retencion_cliente','retencion_proveedor','plazos_clientes','plazos_proveedores').order_by('nombreComercial') 
    if tipo == 'CLIENTE':
        return Terceros.objects.filter(isCliente = True).select_related('vendedor','cuenta_x_cobrar','cuenta_x_pagar','cuenta_saldo_a_cliente','cuenta_saldo_a_proveedor','formaPago','departamento','municipio').prefetch_related('retencion_cliente','retencion_proveedor','plazos_clientes','plazos_proveedores').order_by('nombreComercial')
    if tipo == 'PROVEEDOR':
        return Terceros.objects.filter(isProveedor = True).select_related('vendedor','cuenta_x_cobrar','cuenta_x_pagar','cuenta_saldo_a_cliente','cuenta_saldo_a_proveedor','formaPago','departamento','municipio').prefetch_related('retencion_cliente','retencion_proveedor','plazos_clientes','plazos_proveedores').order_by('nombreComercial')
    

def getTercero(id):
    return Terceros.objects.get(id=id).select_related('vendedor','cuenta_x_cobrar','cuenta_x_pagar','cuenta_saldo_a_cliente','cuenta_saldo_a_proveedor','formaPago','departamento','municipio').prefetch_related('retencion_cliente','retencion_proveedor','plazos_clientes','plazos_proveedores')
   