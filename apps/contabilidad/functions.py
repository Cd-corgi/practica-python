from .models import asiento, asientoDetalle 

def obtener_asiento(numero):
    if asiento.objects.filter(numero = numero).exists():
        asientos = asiento.objects.get(numero = numero)
        return asientos
    else: 
        return None  


def EliminarAsiento(numero):
    resultado = False
    if asiento.objects.filter(numero = numero).exists():
        resultado = True
        consultaAsiento = asiento.objects.get(numero = numero)
        consultaDetalle = asientoDetalle.objects.filter(asiento = consultaAsiento.id)
        consultaDetalle.delete()
        consultaAsiento.delete()
    else: 
        resultado = False
    return resultado                    