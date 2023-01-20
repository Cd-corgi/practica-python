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



    