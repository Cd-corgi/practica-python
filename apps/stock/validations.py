from rest_framework import serializers

def ValidarOrden(orden):

    if orden['numeracion'] == None or orden['numeracion'] == '':
        raise serializers.ValidationError('La numeración no puede quedar nulo o vacio')
    if orden['proveedor'] == None or orden['proveedor'] == '':
        raise serializers.ValidationError('El proveedor no puede quedar nulo o vacio')
    if orden['fecha'] == None or orden['fecha'] == '':
        raise serializers.ValidationError('La fecha no puede quedar nulo o vacio')
    if orden['formaPago'] == None or orden['formaPago'] == '':
        raise serializers.ValidationError('La forma de pago no puede quedar nulo o vacio')
    if orden['usuario'] == None or orden['usuario'] == '':
        raise serializers.ValidationError('el usuario no puede quedar nulo o vacio')

def ValidarIngreso(ingreso):

    if ingreso['numeracion'] == None or ingreso['numeracion'] == '':
        raise serializers.ValidationError('La numeración no puede quedar nulo o vacio')
    if ingreso['orden'] == None or ingreso['orden'] == '':
        raise serializers.ValidationError("La orden no puede quedar nulo o vacaio")
    if ingreso['proveedor'] == None or ingreso['proveedor'] == '':
        raise serializers.ValidationError('El proveedor no puede quedar nulo o vacio')
    if ingreso['fecha'] == None or ingreso['fecha'] == '':
        raise serializers.ValidationError('La fecha no puede quedar nulo o vacio')
    if ingreso['usuario'] == None or ingreso['usuario'] == '':
        raise serializers.ValidationError('El usuario no puede quedar nulo o vacio')
    