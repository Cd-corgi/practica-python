from django.db import models
# from .manager import OrdenManager
# Create your models here.
from datetime import date, timedelta, datetime
from apps.configuracion.models import *
from django.db.models.signals import post_save,post_delete




class Bodega(models.Model):
    """Model definition for Bodega."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Bogeda', max_length=100)

    class Meta:
        """Meta definition for Bodega."""

        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'
        

    def __str__(self):
        return self.nombre

class tipoProducto(models.Model):
    """Model definition for Bodega."""

    # TODO: Define fields here
    id     = models.AutoField(primary_key          = True)
    nombre = models.CharField('ATIPO', max_length = 100)
    c_tipo = models.ForeignKey(to= 'contabilidad.puc',related_name='cuenta_tipo', on_delete=models.PROTECT)

    class Meta:
        """Meta definition for Bodega."""

        verbose_name = 'tipoProducto'
        verbose_name_plural = 'tiposDeProductos'
       

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    id                = models.IntegerField(primary_key = True)  # Field name made lowercase.
    nombre            = models.CharField('Nombre', max_length = 150)
    Filtro            = models.CharField('Filtro', max_length  = 150)
    invima            = models.CharField(max_length           = 50, blank = True, null = True)
    cum               = models.CharField(max_length           = 50, blank = True, null = True)
    valorCompra       = models.FloatField()
    valorVenta        = models.FloatField()
    valorventa1       = models.FloatField()
    valorventa2       = models.FloatField()
    fv                = models.BooleanField(default = True)
    regulado          = models.BooleanField(default = False)
    valorRegulacion   = models.FloatField(default = 0)
    stock_inicial     = models.IntegerField(default = 0)
    stock_min         = models.IntegerField(default = 0)
    stock_max         = models.IntegerField(default = 0)
    tipoProducto      = models.ForeignKey(tipoProducto, related_name="productos_tipo_producto",on_delete=models.PROTECT)
    habilitado        = models.BooleanField(default = True)
    bodega            = models.ForeignKey(Bodega, on_delete=models.PROTECT)
    impuesto          = models.ForeignKey("configuracion.Impuestos", blank=True, null=True, related_name="productos_impuesto",on_delete=models.PROTECT)
    codigoDeBarra     = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    unidad            = models.CharField('Unidad', max_length=150)
    usuario           = models.ForeignKey("users.User", related_name="productos_usuario",on_delete=models.PROTECT)
    creado            = models.DateTimeField(auto_now=True)
    modificado        = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    nombreymarcaunico = models.CharField(unique=True, max_length=900, blank=True, null=True)
    
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        

    def __str__(self):
        return self.nombreymarcaunico

    # def save(self, *args, **kwargs):
    #     t = Terceros.objects.get(documento = "1221981200")
    #     k = Kardex()
    #     k.producto = self       
    #     k.descripcion = "Saldo Inicial"
    #     k.tipo       = "SI"
    #     k.tercero    = t
    #     k.bodega     = self.bodega   
    #     k.unidades   = self.stock_inicial
    #     k.balance    = self.stock_inicial
    #     k.precio     = self.valorCompra
    #     k.save()
    #     super(Productos, self).save(*args, **kwargs)






class Kardex(models.Model):
    """Model definition for Kardex."""
    id          = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length= 250)
    tipo        = models.CharField('tipo', max_length= 50)
    producto    = models.ForeignKey(Productos, related_name="kardexs_producto", on_delete = models.PROTECT)
    tercero     = models.ForeignKey("configuracion.Terceros", related_name="kardexs_terceros",on_delete = models.PROTECT)
    bodega      = models.ForeignKey(Bodega, on_delete= models.PROTECT,related_name = "kardexs_bodega")
    unidades    = models.IntegerField()
    fecha       = models.DateField("fecha:", auto_now=True, auto_now_add=False)
    balance     = models.IntegerField(default= 0)
    precio      = models.FloatField()


    # TODO: Define fields here

    class Meta:
        """Meta definition for Kardex."""

        verbose_name = 'Kardex'
        verbose_name_plural = 'Kardex'
        db_table = 'kardexs'

    def __str__(self):
       return self.descripcion


class Inventario(models.Model):
    """Model definition for Iventario."""
    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    bodega      = models.ForeignKey(Bodega, related_name="inventario_bodega", on_delete=models.PROTECT)
    idProducto  = models.ForeignKey(Productos, related_name="inventario_producto", on_delete=models.PROTECT)
    vencimiento = models.DateField('Fecha vencimiento', auto_now=False, auto_now_add=False, null=True, blank=True)
    valorCompra = models.FloatField()
    unidades    = models.IntegerField()
    lote        = models.CharField('lote', max_length=50)
    estado      = models.BooleanField()
    laboratorio = models.CharField('Laboratorio:', max_length=150, blank=False, null=False)
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return self.lote

class OrdenDeCompra(models.Model):
    """Model definition for OrdenDeCompra"""
    # TODO: Define the fields here
    id          = models.AutoField(primary_key=True)
    numeracion  = models.ForeignKey("configuracion.numeracion", related_name="numeracion_orden", on_delete=models.PROTECT)
    numero      = models.CharField("Numero:", max_length=20, blank=True, null=True)
    consecutivo = models.IntegerField(blank=True, null=True)
    prefijo     = models.CharField("Prefijo:", max_length=20,blank=True, null=True)
    proveedor   = models.ForeignKey("configuracion.Terceros", related_name="Orden_proveedor",on_delete=models.PROTECT)
    fecha       = models.DateTimeField("Fecha:", auto_now=False, auto_now_add=False)
    formaPago   = models.ForeignKey("configuracion.FormaPago", related_name="orden_formaPago",on_delete=models.PROTECT)
    usuario     = models.ForeignKey("users.User", related_name="orden_usuario",on_delete=models.PROTECT)
    observacion = models.TextField(default="", blank=True, null=True)
    subtotal    = models.FloatField()
    iva         = models.FloatField()
    retencion   = models.FloatField()
    ingresada   = models.BooleanField(default = False, blank=True, null=True)
    descuento   = models.FloatField(default = 0)
    total       = models.FloatField()   

    class Meta:
        """Meta definition for OrdenDeCompra"""
        
        verbose_name = "Orden de compra"
        verbose_name_plural = "Orden de Compras"
        db_table = 'ordendecompra'

    def __str__(self):
        return self.numero
    
    
 

class OrdenDetalle(models.Model):
    """Model definition for DettaleOrden"""
    # TODO: Define the fields here
    id          = models.AutoField(primary_key=True)
    orden       = models.ForeignKey(OrdenDeCompra, related_name="detalle_orden",on_delete=models.PROTECT)
    producto    = models.ForeignKey(Productos, related_name="detalleOrden_productos",on_delete=models.PROTECT)
    cantidad    = models.IntegerField()
    valorUnidad = models.FloatField()
    descuento   = models.FloatField(default = 0)
    iva         = models.IntegerField()

    class Meta:
        """Meta definition for DetalleOrden"""

        verbose_name = "Detalle de Orden"
        verbose_name_plural = "Detalle de Ordenes"
        db_table = "ordendetalle"

    def __str__(self):
        return self.orden.numero

class ImpuestoOrden(models.Model):
    """Model definition for ImpuestoOrden"""
    # TODO: Define the fields here
    id          = models.AutoField(primary_key=True)
    orden       = models.ForeignKey(OrdenDeCompra, related_name="impuesto_orden" ,on_delete=models.PROTECT)
    impuesto    = models.ForeignKey("configuracion.Impuestos", related_name="impuestos_orden",on_delete=models.PROTECT)
    base        = models.FloatField()
    procentaje  = models.FloatField()
    total       = models.FloatField()

    class Meta:
        """Meta definition for ImpuestoOrden"""

        verbose_name = "Impuesto de orden"
        verbose_name_plural = "Impuesto de ordenes"
        db_table = "impuesto_orden"

    def __str__(self):
        return self.orden.numero

class RetencionOrden(models.Model):
    """Model definition for RetencionOrden"""
    # TODO: Define the fields here
    id          = models.AutoField(primary_key=True)
    orden       = models.ForeignKey(OrdenDeCompra, related_name="retencion_orden", on_delete=models.PROTECT)
    retencion   = models.ForeignKey("configuracion.Retenciones", related_name="retenciones_orden",on_delete=models.PROTECT)
    base        = models.FloatField()
    porcentaje  = models.FloatField()
    total       = models.FloatField()

    class Meta:
        """Meta definition for RetencionOrden"""

        verbose_name = "Retencion de orden"
        verbose_name_plural = "Retencion de ordenes"
        db_table = "retencionesorden"

    def __str__(self):
        return self.orden.numero               

class Ingreso(models.Model):
    """Model definition for Ingreso."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    numeracion  = models.ForeignKey("configuracion.numeracion", related_name="ingreso_numeracion",on_delete=models.PROTECT)
    numero      = models.CharField("Numero:", max_length=20, blank=True, null=True)
    consecutivo = models.IntegerField(blank=True, null=True)
    prefijo     = models.CharField("Prefijo:", max_length=20,blank=True, null=True)
    orden       = models.ForeignKey(OrdenDeCompra, related_name="ingreso_orden" , on_delete=models.PROTECT)
    factura     = models.CharField("Factura:", max_length=50)
    proveedor   = models.ForeignKey("configuracion.Terceros", related_name="ingreso_proveedor",on_delete=models.PROTECT)
    fecha       = models.DateField("Fecha:", auto_now=False, auto_now_add=False)
    formaPago   = models.ForeignKey("configuracion.FormaPago", related_name="ingreso_formaPago",on_delete=models.PROTECT)
    usuario     = models.ForeignKey("users.User", related_name="ingreso_usuario" ,on_delete=models.PROTECT)
    observacion = models.TextField(default="", blank=True, null=True)
    subtotal    = models.FloatField()
    iva         = models.FloatField()
    retencion   = models.FloatField()
    descuento   = models.FloatField(default = 0)
    total       = models.FloatField()

    class Meta:
        """Meta definition for Ingreso."""

        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        db_table = "ingreso"


    def __str__(self):
        """Unicode representation of Ingreso."""
        return  str(self.numero)
    
class IngresoDetalle(models.Model):
    """Model definition for IngresoDetalle."""

    # TODO: Define fields here
    id               = models.AutoField(primary_key=True)
    ingreso          = models.ForeignKey(Ingreso, related_name="ingreso_detalle" ,on_delete=models.PROTECT)
    producto         = models.ForeignKey(Productos, related_name="ingreso_producto",on_delete=models.PROTECT)
    cantidad         = models.IntegerField()
    fechaVencimiento = models.DateField("Fecha de vencimiento:", auto_now=False, auto_now_add=False, blank=True, null=True)
    laboratorio      = models.CharField("Laboratorio:", max_length=50)
    lote             = models.CharField("Lote:", max_length=50)
    valorUnidad      = models.FloatField()
    descuento        = models.FloatField(default = 0)
    iva              = models.IntegerField()
    subtotal         = models.FloatField()
    total            = models.FloatField()

    class Meta:
        """Meta definition for IngresoDetalle."""

        verbose_name = 'IngresoDetalle'
        verbose_name_plural = 'IngresoDetalles'
        db_table = 'ingresodetalle'

    def __str__(self):
        """Unicode representation of IngresoDetalle."""
        return self.ingreso.numero

class ImpuestoIngreso(models.Model):
    """Model definition for ImpuestoIngreso."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    ingreso     = models.ForeignKey(Ingreso, related_name="impuesto_ingreso", on_delete=models.PROTECT)
    impuesto    = models.ForeignKey("configuracion.Impuestos", related_name="impuestos_ingreso",on_delete=models.PROTECT)
    base        = models.FloatField()
    procentaje  = models.FloatField()
    total       = models.FloatField()

    class Meta:
        """Meta definition for ImpuestoIngreso."""

        verbose_name = 'ImpuestoIngreso'
        verbose_name_plural = 'ImpuestoIngresos'
        db_table = "impuestoingreso"

    def __str__(self):
        """Unicode representation of ImpuestoIngreso."""
        return self.ingreso.numero

class RetencionIngreso(models.Model):
    """Model definition for RetencionIngreso."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    ingreso     = models.ForeignKey(Ingreso, related_name="retencion_ingreso",on_delete=models.PROTECT)
    retencion   = models.ForeignKey("configuracion.Retenciones", related_name="reteciones_ingreso",on_delete=models.PROTECT)
    base        = models.FloatField()
    procentaje  = models.FloatField()
    total       = models.FloatField()

    class Meta:
        """Meta definition for RetencionIngreso."""

        verbose_name = 'RetencionIngreso'
        verbose_name_plural = 'RetencionIngresos'
        db_table = "retencioningreso"

    def __str__(self):
        """Unicode representation of RetencionIngreso."""
        return self.ingreso.numero
        
class CxPCompras(models.Model):
    """Model definition for CxPCompras."""

    # TODO: Define fields here
    id                 = models.AutoField(primary_key=True)
    ingreso            = models.ForeignKey(Ingreso, related_name="cxpcompras_ingreso", on_delete=models.PROTECT)
    factura            = models.CharField("Factura:", max_length=50, blank=True, null=True)
    formaPago          = models.ForeignKey(FormaPago, related_name="cxpcompras_formaPago",on_delete=models.PROTECT, blank=True, null=True)
    fecha              = models.DateField("Fecha:", auto_now=False, auto_now_add=False, blank=True, null=True)
    fechaVencimiento   = models.DateField("Fecha de Vencimiento:", auto_now=False, auto_now_add=False, blank=True, null=True)
    observacion        = models.CharField("Observación:", max_length=120, blank=True, null=True)
    proveedor          = models.ForeignKey("configuracion.Terceros", related_name="cxpcompras_proveedor",on_delete=models.PROTECT)
    base               = models.FloatField(default=0)
    iva                = models.FloatField(default=0)
    valorAbono         = models.FloatField(default=0)
    reteFuente         = models.FloatField(default=0)
    reteIca            = models.FloatField(default=0)
    valorTotal         = models.FloatField(default=0)

    class Meta:
        """Meta definition for CxPCompras."""
        verbose_name = 'CxPCompras'
        verbose_name_plural = 'CxPComprass'
        db_table = 'cxpcompras'

    def __str__(self):
        """Unicode representation of CxPCompras."""
        return 'd'

    def save(self, *args, **kwargs):
        
        self.fecha     = datetime.strptime(self.ingreso.fecha,"%Y-%m-%d")
        self.factura   = self.ingreso.factura
        self.formaPago = self.ingreso.formaPago
        
        if self.formaPago.nombre == 'CONTADO':
            self.fechaVencimiento =  self.fecha
        elif self.formaPago.nombre == 'CREDITO 30 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(30)
        elif self.formaPago.nombre == 'CREDITO 45 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(45)
        elif self.formaPago.nombre == 'CREDITO 60 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(60)
        elif self.formaPago.nombre == 'CREDITO 75 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(75)
        elif self.formaPago.nombre == 'CREDITO 90 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(90)
        elif self.formaPago.nombre == 'CREDITO 120 DIAS':
            self.fechaVencimiento =  self.fecha + timedelta(120)
        else:
            self.fechaVencimiento =  self.fecha
        super(CxPCompras, self).save(*args, **kwargs) # Call the real save() method


class PagosCompras(models.Model):
    """Model definition for PagosCompras."""

    # TIPO TRANSACCIÓN
    SIN_FACTURA = '0'
    CON_FACTURA = '1'

    TIPO_TRANSACCION = (
        (SIN_FACTURA, "Pago sin relación"),
        (CON_FACTURA, "Pago con relación"),
    )

    # TODO: Define fields here
    id              = models.AutoField(primary_key=True)
    numeracion      = models.ForeignKey("configuracion.numeracion", related_name="pagos_numeracion" ,on_delete=models.PROTECT)
    numero          = models.CharField("Numero:", max_length=20, blank=True, null=True)
    consecutivo     = models.IntegerField(blank=True, null=True)
    prefijo         = models.CharField("Prefijo:", max_length=20,blank=True, null=True)
    tipoTransaccion = models.BooleanField('Tipo de transaccion:', choices = TIPO_TRANSACCION )
    ingreso         = models.ForeignKey(Ingreso, related_name="pagos_ingreso",on_delete=models.PROTECT)
    factura         = models.CharField("Factura:", max_length=50)
    usuario         = models.ForeignKey("users.User", related_name="pagos_usuario",on_delete=models.PROTECT)
    fecha           = models.DateField("Fecha:", auto_now=False, auto_now_add=False)
    concepto        = models.TextField("Concepto:")
    ValorAbono      = models.FloatField(default=0)
    descuento       = models.FloatField(default=0)

    class Meta:
        """Meta definition for PagosCompras."""

        verbose_name = 'PagosCompra'
        verbose_name_plural = 'PagosCompras'
        db_table = 'pagoscompras'

    def __str__(self):
        """Unicode representation of PagosCompras."""
        return self.ingreso.numero
        
    def save(self, *args, **kwargs):
       self.consecutivo = self.numeracion.proximaFactura
       self.prefijo     = self.numeracion.prefijo
       self.numero      = self.numeracion.prefijo+'-'+str(self.numeracion.proximaFactura)
       super(PagosCompras, self).save(*args, **kwargs) # Call the real save() method
    

    
class NotaDebito(models.Model):

    ADICION = '1'
    AUMENTO_PRECIO = '2'

    TIPO_DE_NOTA_CHOICES = (
        (ADICION, 'Adición de productos'),
        (AUMENTO_PRECIO, 'Aumento de precios'),
    )

    """Model definition for NotaDebito."""

    # TODO: Define fields here
    id              = models.AutoField(primary_key=True)
    tipoDeNota      = models.CharField("Tipo de nota:", max_length=50, choices=TIPO_DE_NOTA_CHOICES)
    numero          = models.CharField("Numero:", max_length=20, blank=True, null=True)
    consecutivo     = models.IntegerField(blank=True, null=True)
    prefijo         = models.CharField("Prefijo:", max_length=20,blank=True, null=True)
    numeracion      = models.ForeignKey("configuracion.numeracion", related_name="notaDebito_numeracion",on_delete=models.PROTECT)
    factura         = models.CharField("Factura:", max_length=50)
    ingreso         = models.ForeignKey(Ingreso, related_name="notaDebito_ingreso",on_delete=models.PROTECT)
    observacion     = models.TextField(default = "",blank=True, null=True)
    fecha           = models.DateField("Fecha:", auto_now=False, auto_now_add=False)
    valorTotal      = models.FloatField(default = 0)
    iva             = models.FloatField(default = 0)
    retencion       = models.FloatField(default = 0)
    proveedor       = models.ForeignKey("configuracion.Terceros", related_name="notaDebito_proveedor",on_delete=models.PROTECT)
    usuario         = models.ForeignKey("users.User", related_name="notaDebito_usuario",on_delete=models.PROTECT)

    class Meta:
        """Meta definition for NotaDebito."""

        verbose_name = 'NotaDebito'
        verbose_name_plural = 'NotaDebitos'
        db_table = 'notadebitocompras'

    def __str__(self):
        """Unicode representation of NotaDebito."""
        return self.numero
    
    def save(self, *args, **kwargs):
       self.consecutivo = self.numeracion.proximaFactura
       self.prefijo     = self.numeracion.prefijo
       self.numero      = self.numeracion.prefijo+'-'+str(self.numeracion.proximaFactura)
       super(NotaDebito, self).save(*args, **kwargs) # Call the real save() method

class NotaDebitoDetalle(models.Model):
    """Model definition for NotaDebitoDetalle."""

    # TODO: Define fields here

    id          = models.AutoField(primary_key=True)
    nota        = models.ForeignKey(NotaDebito, related_name="detalle_notaDebito",on_delete=models.PROTECT)
    producto    = models.ForeignKey(Productos, related_name="producto_notaDebito",on_delete=models.PROTECT)
    lote        = models.CharField("Lote:", max_length=50)
    cantidad    = models.IntegerField()
    valorUnidad = models.FloatField()
    iva         = models.FloatField(default = 0)
    subtotal    = models.FloatField()

    class Meta:
        """Meta definition for NotaDebitoDetalle."""

        verbose_name = 'NotaDebitoDetalle'
        verbose_name_plural = 'NotaDebitoDetalles'
        db_table = 'notadebitodetallecompras'

    def __str__(self):
        """Unicode representation of NotaDebitoDetalle."""
        return self.nota.numero


class NotaCredito(models.Model):

    DEVOLUCION = '1'
    REBAJA_PRECIO = '2'
    REBAJA_PARCIAL_TOTAL = '3'
    CORRECION = '4'

    TIPO_DE_NOTAS_CHOICES = (
        (DEVOLUCION, 'Devoluciones'),
        (REBAJA_PRECIO, 'Rebajas o disminución de precio'),
        (REBAJA_PARCIAL_TOTAL, 'Rebajas o descuento parcial o total'),
        (CORRECION, 'Correción a item'),
    )

    FACTURA = 'FACTURA'
    FECHA = 'FECHA'
    ITEM = 'ITEM'

    CORRECION_CHOICES = (
        (FACTURA, 'Correción factura'),
        (FECHA, 'Correción fecha'),
        (ITEM, 'Correción item'),
    )

    """Model definition for NotaCredito."""

    # TODO: Define fields here
    id              = models.AutoField(primary_key=True)  
    numeracion      = models.ForeignKey("configuracion.numeracion", related_name="NotaCredito_numeracion",on_delete=models.PROTECT)
    numero          = models.CharField("Numero:", max_length=20, blank=True, null=True)
    consecutivo     = models.IntegerField(blank=True, null=True)
    prefijo         = models.CharField("Prefijo:", max_length=20,blank=True, null=True)
    tipoNota        = models.CharField("Tipo de nota:", max_length=50, choices=TIPO_DE_NOTAS_CHOICES)
    tipoCorrecion   = models.CharField("Tipo de correccion:", max_length=50, choices=CORRECION_CHOICES , null=True, blank=True)
    ingreso         = models.ForeignKey(Ingreso, related_name="NotaCredito_ingreso",on_delete=models.PROTECT)
    proveedor       = models.ForeignKey("configuracion.Terceros", related_name="NotaCredito_proveedor",on_delete=models.PROTECT)
    factura         = models.CharField("Factura:", max_length=50)
    contabilizado   = models.BooleanField(default=False)
    observacion     = models.TextField(default = "", blank=True, null=True)
    numeroNota      = models.CharField("Numero de nota:", max_length=50, null=True, blank=True)
    


    class Meta:
        """Meta definition for NotaCredito."""

        verbose_name = 'NotaCredito'
        verbose_name_plural = 'NotaCreditos'
        db_table = 'notacreditocompras'

    def __str__(self):
        """Unicode representation of NotaCredito."""
        return self.numero
    
    def save(self, *args, **kwargs):
       self.consecutivo = self.numeracion.proximaFactura
       self.prefijo     = self.numeracion.prefijo
       self.numero      = self.numeracion.prefijo+'-'+str(self.numeracion.proximaFactura)
       super(NotaCredito, self).save(*args, **kwargs) # Call the real save() method
    
class DetalleNotaCredito(models.Model):
    """Model definition for DetalleNotaCredito."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    nota        = models.ForeignKey(NotaCredito, related_name="detalle_NotaCredito" , on_delete=models.PROTECT)
    producto    = models.ForeignKey(Productos, related_name = "prdoucto_notaCreditoDetalle", on_delete=models.PROTECT)
    lote        = models.CharField("Lote:", max_length=50)
    cantidad    = models.IntegerField()
    valorUnidad = models.FloatField()
    iva         = models.FloatField(default=0)
    subtotal    = models.FloatField()


    class Meta:
        """Meta definition for DetalleNotaCredito."""

        verbose_name = 'DetalleNotaCredito'
        verbose_name_plural = 'DetalleNotaCreditos'
        db_table = 'notacreditodetalle'

    def __str__(self):
        """Unicode representation of DetalleNotaCredito."""
        return self.nota.numero
