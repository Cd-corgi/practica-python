from .models import *
from apps.configuracion.models import Terceros

def saldoInicialStock(sender,instance,**kwargs):
    if instance.stock_inicial > 0:
        t = Terceros.objects.get(documento = "1221981200")
        k = Kardexs()
        l.producto = instance.id       
        k.descripcion = "Saldo Inicial"
        k.tipo       = "SI"
        k.tercero    = t
        k.bodega     = instance.bodega   
        k.unidades   = instance.stock_inicial
        k.balance    = instance.stock_inicial
        k.precio     = instance.valorCompra
        k.save()
