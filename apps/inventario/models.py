from django.db import models
# from .manager import OrdenManager
# Create your models here.
from datetime import date, timedelta
from apps.configuracion.models import *
from django.db.models.signals import post_save,post_delete

from .signals import *

# class TimeLine(models.Model):
#     """Model definition for TimeLine."""

#     # TODO: Define fields here
#     fecha_creacion     = models.DateTimeField('fecha Creacion:', auto_now=True)
#     fecha_modificacion = models.DateTimeField('fecha Creacion:', auto_now_add=True)
#     usuario            = models.ForeignKey("users.User", on_delete=models.PROTECT)
#     empresa            = models.ForeignKey("configuracion.Empresa", on_delete=models.PROTECT)
#     estado             = models.BooleanField(default = True)

#     class Meta:
#         """Meta definition for TimeLine."""
#         abstract = True
        

# class Marca(TimeLine,models.Model):
#     """Model definition for Marca."""

#     # TODO: Define fields here
#     id = models.AutoField(primary_key = True)
#     nombre = models.CharField('nombre', max_length=70)
#     class Meta:
#         """Meta definition for Marca."""

#         verbose_name = 'Marca'
#         verbose_name_plural = 'Marcas'

#     def __str__(self):
#         return self.nombre

# class Unidad(TimeLine,models.Model):
#     """Model definition for Marca."""

#     # TODO: Define fields here
#     id = models.AutoField(primary_key = True)
#     nombre = models.CharField('nombre', max_length=70)
#     class Meta:
#         """Meta definition for Unidad."""

#         verbose_name = 'Unidad'
#         verbose_name_plural = 'Unidades'

#     def __str__(self):
#         return self.nombre


    
class Bodega(models.Model):
    """Model definition for Bodega."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Bogeda', max_length=100)

    class Meta:
        """Meta definition for Bodega."""

        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'
        db_table = "bodega"

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
        db_table = "tipoProducto"

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    id                = models.IntegerField(primary_key = True)  # Field name made lowercase.
    nombre            = models.CharField('Nombre', max_length = 150)
    marca             = models.CharField('Marca', max_length  = 150)
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
    tipoProducto      = models.ForeignKey(tipoProducto, on_delete=models.PROTECT)
    habilitado        = models.BooleanField(default = True)
    bodega            = models.ForeignKey(Bodega, on_delete=models.PROTECT)
    impuesto          = models.ForeignKey("configuracion.Impuestos", on_delete=models.PROTECT)
    codigoDeBarra     = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    unidad            = models.CharField('Unidad', max_length=150)
    usuario           = models.ForeignKey("users.User", on_delete=models.PROTECT)
    creado            = models.DateTimeField(auto_now=True)
    modificado        = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    nombreymarcaunico = models.CharField(unique=True, max_length=900, blank=True, null=True)
    
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = "productos"

    def __str__(self):
        return self.nombreymarcaunico

#     def save(self, *args, **kwargs):
#         code = self.nombre[0:3]
#         p = Productos.objects.filter(nombre__icontains=code)
#         n = p.count() + 1
#         self.codigoDeBarra = code+str(n).rjust(2, '0')
#         invima = ""
#         cum = ""
#         if self.invima != "":
#             invima = 'INV:'+self.invima
#         if self.cum != "":
#             cum = 'CUM:'+self.cum
#         self.nombreymarcaunico = self.nombre+'('+self.marca.nombre+') '+self.unidad.nombre+' '+invima+' '+cum
#         super(Productos, self).save(*args, **kwargs)


class Inventario(models.Model):
    """Model definition for Iventario."""
    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    bodega      = models.ForeignKey(Bodega, related_name="inventario_bodega", on_delete=models.PROTECT)
    idProducto  = models.ForeignKey(Productos, on_delete=models.PROTECT)
    vencimiento = models.DateField('Fecha vencimiento', auto_now=False, auto_now_add=False, null=True, blank=True)
    unidades    = models.IntegerField()
    lote        = models.CharField('lote', max_length=50)
    estado      = models.BooleanField()
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Iventario'
        verbose_name_plural = 'Iventarios'

    def __str__(self):
        return self.lote



# class OrdenDeCompra(TimeLine,models.Model):
#     """Model definition for OrdenDeCompra."""
#     id = models.AutoField(primary_key=True)
#     factura = models.CharField(max_length=250,default = "100")
#     tercero = models.ForeignKey('configuracion.Terceros', on_delete=models.PROTECT,related_name="orden_tercero")
#     iva = models.FloatField()
#     fecha_vencimiento = models.DateField('Fecha_vence', auto_now=False, auto_now_add=False, null = True , blank = True)
#     descuento = models.FloatField()
#     retencion = models.FloatField()
#     total = models.FloatField()
#     observaciones = models.CharField('Observaciones', max_length=250, null=True,blank=True)
  
#     # TODO: Define fields here

#     objects = OrdenManager()

#     class Meta:
#         """Meta definition for OrdenDeCompra."""

#         verbose_name = 'Orden de compra'
#         verbose_name_plural = 'Ordenes de compras'

#     def __str__(self):
#        return self.tercero.nombreComercial



#     def save(self, *args, **kwargs):
#         tercero = self.tercero
        
#         if tercero.formaPago.nombre == 'CONTADO':
#             self.fecha_vencimiento =  date.today()
#         if tercero.formaPago.nombre == 'CREDITO 30 DIAS':
#             td = timedelta(30)
#             self.fecha_vencimiento =  date.today() + td
#         if tercero.formaPago.nombre == 'CREDITO 45 DIAS':
#             td = timedelta(45)
#             self.fecha_vencimiento =  date.today() + td
#         if tercero.formaPago.nombre == 'CREDITO 60 DIAS':
#             td = timedelta(60)
#             self.fecha_vencimiento =  date.today() + td
#         if tercero.formaPago.nombre == 'CREDITO 90 DIAS':
#             td = timedelta(90)
#             self.fecha_vencimiento =  date.today() + td
        
#         super(OrdenDeCompra, self).save(*args, **kwargs)
    

# class OrdenDeCompraDetalle(models.Model):
#     """Model definition for OrdenDeCompraDetalle."""
#     id = models.AutoField(primary_key=True)
#     orden = models.ForeignKey(OrdenDeCompra, on_delete=models.PROTECT, related_name="orden_detalle")
#     producto = models.ForeignKey(Productos, on_delete=models.PROTECT,related_name="orden_producto")
#     cantidad = models.IntegerField()
#     valorUnidad = models.FloatField()
#     iva = models.FloatField()
#     descuento = models.FloatField()
#     total = models.FloatField()
#     # TODO: Define fields here

#     class Meta:
#         """Meta definition for OrdenDeCompraDetalle."""

#         verbose_name = 'OrdenDeCompraDetalle'
#         verbose_name_plural = 'OrdenDeCompraDetalles'

#     def __str__(self):
#         return self.producto.nombreymarcaunico



# class IngresoCompras(TimeLine,models.Model):
#     """Model definition for IngresoCompras."""
#     id = models.AutoField(primary_key=True)
#     orden = models.ForeignKey(OrdenDeCompra, on_delete=models.PROTECT, related_name="orden_ingreso")
#     fechaFactura = models.DateField('fecha Factura', auto_now=False, auto_now_add=False)
#     factura = models.CharField('factura', max_length=50, unique=True)
#     iva = models.FloatField()
#     descuento = models.FloatField()
#     retencion = models.FloatField()
#     total = models.FloatField()

#     # TODO: Define fields here

#     class Meta:
#         """Meta definition for IngresoCompras."""

#         verbose_name = 'IngresoCompras'
#         verbose_name_plural = 'IngresoCompras'

#     def __str__(self):
#         return self.factura


# class IngresoComprasDetalle(models.Model):
#     """Model definition for IngresoComprasDetalle."""
#     id = models.AutoField(primary_key=True)
#     ingreso = models.ForeignKey(IngresoCompras, on_delete=models.PROTECT, related_name="ingreso_detalle")
#     producto = models.ForeignKey(Productos, on_delete=models.PROTECT,related_name="ingreso_producto")
#     lote = models.CharField('lote', max_length=50)
#     fechaVence = models.DateField('Fecha vencimiento:', auto_now=False, auto_now_add=False)
#     cantidad = models.IntegerField()
#     valorUnidad = models.FloatField()
#     iva = models.FloatField()
#     descuento = models.FloatField()
#     total = models.FloatField()
#     # TODO: Define fields here

#     class Meta:
#         """Meta definition for IngresoComprasDetalle."""

#         verbose_name = 'IngresoComprasDetalle'
#         verbose_name_plural = 'IngresoComprasDetalles'

#     def __str__(self):
#         return self.producto.nombreymarcaunico

# class StockProducto(TimeLine,models.Model): 
#     """Model definition for StockProducto."""
#     # TODO: Define fields here
#     id          = models.AutoField(primary_key=True)
#     bodega      = models.ForeignKey(Bodega, on_delete=models.PROTECT,related_name="stock_bodega")
#     producto    = models.ForeignKey(Productos, on_delete=models.PROTECT,related_name="stock_producto")
#     unidades    = models.IntegerField()
#     valorCompra = models.FloatField()
#     lote        = models.CharField('lote', max_length=50, unique=True)
#     estado      = models.BooleanField(default=True)
    
#     class Meta:
#         """Meta definition for StockProducto."""

#         verbose_name = 'StockProducto'
#         verbose_name_plural = 'StockProductos'

#     def __str__(self):
#         return self.producto.nombreymarcaunico

class Kardex(models.Model):
    """Model definition for Kardex."""
    id          = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length= 250)
    tipo        = models.CharField('tipo', max_length= 50)
    producto    = models.ForeignKey(Productos, related_name="kardex_producto", on_delete = models.PROTECT)
    tercero     = models.ForeignKey("configuracion.Terceros", on_delete = models.PROTECT)
    bodega      = models.ForeignKey(Bodega, on_delete= models.PROTECT,related_name = "kardex_bodega")
    unidades    = models.IntegerField()
    balance     = models.IntegerField(default= 0)
    precio      = models.FloatField()


    # TODO: Define fields here

    class Meta:
        """Meta definition for Kardex."""

        verbose_name = 'Kardex'
        verbose_name_plural = 'Kardex'
        db_table = 'kardex'

    def __str__(self):
        self.descripcion








class ProductosSumi(models.Model):
    id                = models.IntegerField(primary_key = True)  # Field name made lowercase.
    nombre            = models.CharField('Nombre', max_length = 150)
    marca             = models.CharField('Marca', max_length  = 150)
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
    tipoProducto      = models.ForeignKey(tipoProducto, on_delete=models.PROTECT)
    habilitado        = models.BooleanField(default = True)
    bodega            = models.ForeignKey(Bodega, on_delete=models.PROTECT)
    impuesto          = models.ForeignKey("configuracion.Impuestos", on_delete=models.PROTECT)
    codigoDeBarra     = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    unidad            = models.CharField('Unidad', max_length=150)
    usuario           = models.ForeignKey("users.User", on_delete=models.PROTECT)
    creado            = models.DateTimeField(auto_now=True)
    modificado        = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    nombreymarcaunico = models.CharField(unique=True, max_length=900, blank=True, null=True)
    
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = "productosSumi"

    def __str__(self):
        return self.nombreymarcaunico



class Kardexs(models.Model):
    """Model definition for Kardex."""
    id          = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length= 250)
    tipo        = models.CharField('tipo', max_length= 50)
    producto    = models.ForeignKey(ProductosSumi, related_name="kardexs_producto", on_delete = models.PROTECT)
    tercero     = models.ForeignKey("configuracion.Terceros", on_delete = models.PROTECT)
    bodega      = models.ForeignKey(Bodega, on_delete= models.PROTECT,related_name = "kardexs_bodega")
    unidades    = models.IntegerField()
    balance     = models.IntegerField(default= 0)
    precio      = models.FloatField()


    # TODO: Define fields here

    class Meta:
        """Meta definition for Kardex."""

        verbose_name = 'Kardex'
        verbose_name_plural = 'Kardex'
        db_table = 'kardexs'

    def __str__(self):
        self.descripcion

class Inventarios(models.Model):
    """Model definition for Iventario."""
    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    bodega      = models.ForeignKey(Bodega, related_name="inventarios_bodega", on_delete=models.PROTECT)
    idProducto  = models.ForeignKey(ProductosSumi, on_delete=models.PROTECT)
    vencimiento = models.DateField('Fecha vencimiento', auto_now=False, auto_now_add=False, null=True, blank=True)
    unidades    = models.IntegerField()
    lote        = models.CharField('lote', max_length=50)
    estado      = models.BooleanField()
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Iventario'
        verbose_name_plural = 'Iventarios'

    def __str__(self):
        return self.lote




post_save.connect(saldoInicialStock,sender=ProductosSumi)





