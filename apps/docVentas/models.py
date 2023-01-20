from django.db import models
from apps.users.models import User
from apps.configuracion.models import numeracion
from datetime import date, timedelta


class CxcMovi(models.Model):
    """Model definition for CxcMovi."""


    # TODO: Define fields here
    id               = models.AutoField(primary_key = True)
    numeracion       = models.ForeignKey(to="configuracion.numeracion", related_name="numeracion_factura", on_delete=models.PROTECT)
    consecutivo      = models.IntegerField()
    prefijo          = models.CharField('prefijo', max_length=50)
    cliente          = models.ForeignKey("configuracion.Terceros",models.PROTECT)
    valor            = models.FloatField()
    fecha            = models.DateField('Fecha', auto_now=True, auto_now_add=False)
    fechaVencimiento = models.DateField('Fecha de vencimiento', auto_now=False, auto_now_add=False)
    abono            = models.FloatField(default = 0)
    descuento        = models.FloatField(default = 0)
    valorDomicilio   = models.FloatField(default = 0)
    valorLetras      = models.CharField('Valor en letras', max_length=250)
    observacion      = models.CharField('Observacion', max_length=350,blank=True, null=True)
    formaPago        = models.ForeignKey(to='configuracion.FormaPago', related_name="cxc_formaPago", on_delete=models.PROTECT)
    vendedor         = models.ForeignKey(to="configuracion.VendedoresClientes", related_name="facturas_vendedor", on_delete=models.PROTECT)
    pagada           = models.BooleanField(default = False)
    usuario          = models.ForeignKey("users.User",models.PROTECT)
    xmlEstado        = models.BooleanField(default = False)
    cufe             = models.CharField('cufe', max_length=350, blank=True, null=True)
    qr               = models.CharField('qr', max_length=350, blank=True, null=True)
    statusFac        = models.CharField('statusFac', max_length=350, blank=True, null=True)
    valorReteFuente  = models.FloatField(default = 0)
    valorReteIca     = models.FloatField(default = 0)
    valorReteCree    = models.FloatField(default = 0)
    despachado       = models.BooleanField(default = False)
    correoEnviado    = models.BooleanField(default = False)

    class Meta:
        """Meta definition for CxcMovi."""

        verbose_name = 'CxcMovi'
        verbose_name_plural = 'CxcMovi'

    def __str__(self): 
        return f'{self.id}, {self.fechaCreacion}'
    
    def save(self, *args, **kwargs):
        consecutivo = self.numeracion.proximaFactura
        prefijo     = self.numeracion.prefijo
        vendedor    = self.cliente.vendedor
     
        if self.formaPago.nombre == 'CONTADO':
            self.fecha_vencimiento =  date.today()
        if self.formaPago.nombre == 'CREDITO 30 DIAS':
            td = timedelta(30)
            self.fecha_vencimiento =  date.today() + td
        if self.formaPago.nombre == 'CREDITO 45 DIAS':
            td = tercerotimedelta(45)
            self.fecha_vencimiento =  date.today() + td
        if self.formaPago.nombre == 'CREDITO 60 DIAS':
            td = timedelta(60)
            self.fecha_vencimiento =  date.today() + td
        if self.formaPago.nombre == 'CREDITO 90 DIAS':
            td = timedelta(90)
            self.fecha_vencimiento =  date.today() + td
        super(CxcMovi, self).save(*args, **kwargs)


class CxcMoviDetalle(models.Model):
    """Model definition for CxcMoviDetalle."""

    # TODO: Define fields here
    id        = models.AutoField(primary_key = True)
    factura   = models.ForeignKey(CxcMovi, related_name="detalle_factura", on_delete=models.PROTECT)
    producto  = models.ForeignKey("stock.Productos", on_delete=models.PROTECT)
    valor     = models.FloatField()
    total     = models.FloatField()
    totalIva  = models.FloatField()
    total     = models.FloatField()
    cantidad  = models.IntegerField()
    descuento = models.FloatField(default = 0)
    lote      = models.CharField('lote', max_length=150)
    iva       = models.FloatField(default = 0)


    class Meta:
        """Meta definition for CxcMoviDetalle."""

        verbose_name = 'CxcMoviDetalle'
        verbose_name_plural = 'CxcMoviDetalles'

    def __str__(self): 
        return f'{self.id}, {self.producto.nombre}'