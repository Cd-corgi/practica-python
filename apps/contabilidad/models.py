from django.db import models
from django.db.models.signals import post_save,post_delete

from .signal import *
from .manager import *

from apps.users.models import User

import locale
# Setea la variable LC_ALL al conjunto de código UTF-8 con descripción español España
#locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')



from apps.configuracion.models import *

class puc(models.Model):
    """Model definition for puc."""
    CLASE        = 'CLASES'
    SUBCLASE     = 'SUBCLASE'
    GRUPO        = 'GRUPO'
    CUENTA       = 'CUENTAS'
    SUBCUENTA    = 'SUBCUENTA'


    DEUDORA      = 'DEUDORA'
    ACREEDORA    = 'ACREEDORA'

    NATURALEZA_CHOICES = (
        (DEUDORA, 'Deudora'),
        (ACREEDORA, 'Acreedora'),
    )

    TIPOSCUENTAS_CHOICES = (
        (CLASE, 'CLASE'),
        (SUBCLASE, 'SUBCLASE'),
        (GRUPO, 'GRUPO'),
        (CUENTA, 'CUENTAS'),
        (SUBCUENTA, 'SUBCUENTA'),
    )

    id               = models.AutoField(primary_key=True)
    tipoDeCuenta     = models.CharField('Tipo de Cuenta:', max_length=15,blank=False, null=False,choices=TIPOSCUENTAS_CHOICES)
    naturaleza       = models.CharField('Naturaleza de la Cuenta:', max_length=20,blank=False, null=False,choices=NATURALEZA_CHOICES)
    nombre           = models.CharField('Nombre de la cuenta:', max_length=100,blank=False, null=False)
    codigo           = models.IntegerField('Codigo de la cuenta:', unique = True,blank=True, null=True)
    estadoFinanciero = models.BooleanField(blank=True, null=True)
    estadoResultado  = models.BooleanField(blank=True, null=True)
    padre            = models.CharField('Padre:', max_length=100,blank=True, null=True)
    

    objects = pucManager()

    # TODO: Define fields here

    class Meta:
        """Meta definition for puc."""

        verbose_name = 'puc'
        verbose_name_plural = 'puc'
        db_table = 'puc'

    def __str__(self):
        return self.nombre


class asiento(models.Model):
    """Model definition for asiento."""
    id           = models.AutoField(primary_key=True)
    numero       = models.CharField('Asiento contable:', max_length=50,blank=False, null=False, unique = True)
    fecha        = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    mes          = models.CharField('Mes:', max_length=50,blank=True, null=True)
    anio         = models.CharField('Año:', max_length=50,blank=True, null=True)
    empresa      = models.ForeignKey(to='configuracion.Empresa', related_name='asiento_empresa', on_delete=models.PROTECT)
    usuario      = models.ForeignKey(User, related_name='asiento_usuario', on_delete=models.PROTECT)
    totalDebito  = models.FloatField('Total crédito:')
    totalCredito = models.FloatField('Total débito:')



    # TODO: Define fields here

    objects = asientoManager()

    class Meta:
        """Meta definition for asiento."""

        verbose_name = 'asiento'
        verbose_name_plural = 'asientos'
        db_table = 'asiento'

    def save(self, *args, **kwargs):
        self.mes  = self.fecha.strftime('%B')
        self.anio  = self.fecha.year
        super(asiento, self).save(*args, **kwargs)


    def __str__(self):
        return self.numero


class asientoDetalle(models.Model):
    id      = models.AutoField(primary_key = True)
    asiento = models.ForeignKey(asiento, related_name='asiento_detalle', on_delete=models.PROTECT)
    tercero = models.ForeignKey(to='configuracion.Terceros', related_name='asiento_tercero', on_delete=models.PROTECT)
    cuenta  = models.ForeignKey(puc, related_name='asiento_cuenta', on_delete=models.PROTECT)
    debito  = models.FloatField('Débito', default   = 0)                  
    credito = models.FloatField('credito', default  = 0)           
    fecha   = models.DateField('Fecha', auto_now=False, auto_now_add=False,blank=True, null=True)
    mes     = models.CharField('Mes:', max_length=50,blank=True, null=True)
    anio    = models.CharField('Año:', max_length=50,blank=True, null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for asientoDetalle."""

        verbose_name = 'asientoDetalle'
        verbose_name_plural = 'asientoDetalles'
        db_table = 'asientoDetalle'


    def save(self, *args, **kwargs):
        self.fecha = self.asiento.fecha
        self.mes   = self.asiento.fecha.strftime('%B')
        self.anio  = self.asiento.fecha.year
        super(asientoDetalle, self).save(*args, **kwargs)


    def __str__(self):
       return self.asiento.numero


class ComprobantesContable(models.Model):
    """Model definition for ComprobantesContable."""
    id             = models.AutoField(primary_key=True)
    numeracion     = models.ForeignKey(to='configuracion.numeracion', related_name='numeracion_comprobante', on_delete=models.PROTECT)
    numero         = models.CharField('Numero:', max_length=50, unique = True,blank=True, null=True)
    consecutivo    = models.IntegerField('Consecutivo:',blank=True, null=True)
    referencia     = models.CharField('Referencia', max_length=50,blank=True, null=True)
    empresa        = models.ForeignKey(to='configuracion.Empresa', related_name='comprobante_empresa', on_delete=models.PROTECT)
    usuario        = models.ForeignKey(User, related_name='comprobante_usuario', on_delete=models.PROTECT)
    total          = models.FloatField('Total Comprobante:', default = 0)
    observaciones  = models.CharField('Observaciones', max_length=500,blank=True, null=True)
    fecha          = models.DateField('Fecha', auto_now=False, auto_now_add=False,blank=True, null=True)
    mes            = models.CharField('Mes:', max_length=50,blank=True, null=True)
    anio           = models.CharField('Año:', max_length=50,blank=True, null=True)

    # TODO: Define fields here


    objects = comprobantesManager()

    class Meta:
        """Meta definition for ComprobantesContable."""

        verbose_name        = 'ComprobantesContable'
        verbose_name_plural = 'ComprobantesContables'
        db_table            = 'comprobantesContables'

    def save(self, *args, **kwargs):
        self.numero      = self.numeracion.prefijo+'-'+self.numeracion.proximaFactura
        self.consecutivo = self.numeracion.proximaFactura
        self.mes         = self.fecha.strftime('%B')
        self.anio        = self.fecha.year
        super(ComprobantesContable, self).save(*args, **kwargs)


    def __str__(self):
        return self.referencia


class CombrobantesDetalleContable(models.Model):
    """Model definition for CombrobantesDetalleContable."""
    id           = models.AutoField(primary_key=True)
    comprobante  = models.ForeignKey(ComprobantesContable, related_name='comprobante_detalle', on_delete=models.PROTECT)  
    tercero      = models.ForeignKey(to='configuracion.Terceros', related_name='cd_tercero', on_delete=models.PROTECT)
    cuenta       = models.ForeignKey(puc, related_name='cd_cuenta', on_delete=models.PROTECT)
    descripcion  = models.CharField('Descripción', max_length=500,blank=True, null=True)
    debito       = models.FloatField('Débito', default   = 0)                  
    credito      = models.FloatField('credito', default  = 0)                  
    fecha        = models.DateField('Fecha', auto_now=False, auto_now_add=False,blank=True, null=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for CombrobantesDetalleContable."""

        verbose_name        = 'CombrobantesDetalleContable'
        verbose_name_plural = 'CombrobantesDetalleContables'
        db_table            = 'CombrobantesDetalleContables'

    def __str__(self):
        return self.comprobante.numero





# signals para el modelo Asiento detalle & Asiento
post_save.connect(update_credito_debito_asiento,sender=asientoDetalle)
post_delete.connect(delete_credito_debito_asiento,sender=asientoDetalle)







