from .models import *

class tiposMercancia():

    valor:float
    tipoDeProducto:tipoProducto
    cuenta:any


    def __init__(self,tipo,cuenta,valor):

        self.tipoDeProducto = tipo
        self.cuenta         = cuenta
        self.valor          = valor