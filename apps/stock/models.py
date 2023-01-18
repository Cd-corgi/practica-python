from django.db import models
# from .manager import OrdenManager
# Create your models here.
from datetime import date, timedelta
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
    class Meta:
        """Meta definition for Iventario."""

        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return self.lote




