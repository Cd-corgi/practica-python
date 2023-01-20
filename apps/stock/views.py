from django.shortcuts import render

from .models import *
from .serializers import *
from apps.users.models import User
from apps.configuracion.models import Impuestos

from .functions import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



import openpyxl
@csrf_exempt
@api_view(('GET','POST'))
def SetProduc(request):

    if request.method == "GET":
        book = openpyxl.load_workbook('productos.xlsx',data_only=True)
        hoja = book.active

        celdas = hoja['A2':'R3245']

        lista_productos = []

        lista_p = []
        lista_k = []
        for fila in celdas:
            producto = [celda.value for celda in fila]
            lista_productos.append(producto)

        
        usuario = User.objects.get(id=1)
        imp = Impuestos.objects.get(id=1)
        for p in lista_productos:
            tipo = tipoProducto.objects.get(id = p[5])
            product = Productos()
           
            product.id       = p[0]    
            product.nombre      =p[2]     
            product.marca        =p[4]     
            product.Filtro       =p[11]      
            product.invima      =p[12]       
            product.cum          =p[13]    
            product.valorCompra  =str(p[9]).replace(",", ".")
            product.valorVenta   =str(p[6]).replace(",", ".")
            product.valorventa1    =str(p[7]).replace(",", ".") 
            product.valorventa2     =str(p[8]).replace(",", ".")  
            product.fv               =p[14]  
            product.stock_inicial    =p[15] 
            

            product.tipoProducto     = tipo
        
            if p[16] ==0:
                b = Bodega.objects.get(id=1)
                product.bodega = b
            if p[16] ==1:
                b = Bodega.objects.get(id=3)
                product.bodega = b
            if p[16] ==2:
                b = Bodega.objects.get(id=2)
                product.bodega = b


            if p[17] != '0':
                product.impuesto = imp
                    
            product.codigoDeBarra   =p[1] 
            product.unidad        =p[10]   
            product.usuario = usuario       
                  
            product.nombreymarcaunico =p[3]


            lista_p.append(product)
          
        Productos.objects.bulk_create(lista_p)

        balances = Productos.objects.filter(stock_inicial__gt = 0)
        t = Terceros.objects.get(documento = "1221981200")
        for x in balances:
           
            k = Kardex()
            k.producto = x      
            k.descripcion = "Saldo Inicial"
            k.tipo       = "SI"
            k.tercero    = t
            k.bodega     = x.bodega   
            k.unidades   = x.stock_inicial
            k.balance    = x.stock_inicial
            k.precio     = x.valorCompra
            k.save()


@csrf_exempt
@api_view(('GET','POST'))
def SetInven(request):

    if request.method == "GET":
        book = openpyxl.load_workbook('inventario.xlsx',data_only=True)
        hoja = book.active

        celdas = hoja['A2':'F1012']

        lista_productos = []

        lista_p = []
        lista_k = []
        for fila in celdas:
            producto = [celda.value for celda in fila]
            lista_productos.append(producto)

        
       
        for p in lista_productos:
            try:
               x = Productos.objects.get(id=p[0])
            except Productos.DoesNotExist:
                print(p[0])
            
            
            
            i = Inventario()
         
            i.bodega = x.bodega     
            i.idProducto = x
            i.vencimiento = p[1]
            i.valorCompra = p[3]
            i.unidades  =p[5] 
            i.lote    =p[2]   
            i.estado  =p[4] 

            i.save()


            
@csrf_exempt
@api_view(('GET','POST'))
def getProductos(request):

    # TIPOS
    # getProductos_SinStock
    # getProductosConsumo__SinStock
    # getKardex
    # getInventario
    # getProductosConsumoStock
    # getProductosVentas

    if request.method == "GET":
        if request.GET.get('getProductosVentas'):
            productos = getProductosVentas()
            return Response(ProductosSerializer(productos, many = True).data)

        if request.GET.get('id'):
            id = request.GET.get('id')
            print(id)
            inventario = getInventario(id)
            return Response(InventarioSerializer(inventario, many = True).data)




            




# class ProductosApiView(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes     = [IsAuthenticated]
#     serializer_class         = ProductosCreateSerializer

#     def get(self, request, format=None):
#         productos = Productos.objects.select_related('unidad','empresa','marca','bodega','usuario').all()
#         return Response(ProductosCreateSerializer(productos, many = True).data)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def put(self, request, format=None):
#         pass

#     def delete(self, request, format=None):
#         pass



# class MarcaApiView(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes     = [IsAuthenticated]
#     serializer_class         = MarcaCreateSerializer

#     def get(self, request, format=None):
#         marca = Marca.objects.all()
#         return Response(MarcaCreateSerializer(marca, many = True).data)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def put(self, request, format=None):
#         pass

#     def delete(self, request, format=None):
#         pass

# class UnidadApiView(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes     = [IsAuthenticated]
#     serializer_class         = UnidadCreateSerializer

#     def get(self, request, format=None):
#         und = Unidad.objects.all()
#         return Response(UnidadCreateSerializer(und, many = True).data)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def put(self, request, format=None):
#         pass

#     def delete(self, request, format=None):
#         pass

# class BodegaApiView(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes     = [IsAuthenticated]
#     serializer_class         =  BodegaCreateSerializer

#     def get(self, request, format=None):
#         bodega = Bodega.objects.all()
#         return Response(BodegaCreateSerializer(bodega, many = True).data)

#     def post(self, request, format=None):
#         print(self.request.data)
#         serializer = self.serializer_class(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def put(self, request, format=None):
#         pass

#     def delete(self, request, format=None):
#         pass

# class OrdenDeCompraApiView(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes     = [IsAuthenticated]
#     serializer_class         = OrdenDeCompraCreateSerializer

#     def get(self, request, format=None):
#         orden = OrdenDeCompra.objects.getOrdenes()
#         return Response(OrdenDeCompraListSerializer(orden, many = True).data)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=self.request.data)
#         print(self.request.data)
#         serializer.is_valid(raise_exception=True)
#         import copy
#         orden = serializer.validated_data.copy()
#         print(orden)
#         productos = orden.pop('orden_detalle')

#         newOrden = OrdenDeCompra(**orden)
#         newOrden.save()

#         for p in productos:
#             newOrdenDetalle = OrdenDeCompraDetalle(orden = newOrden, **p)
#             newOrdenDetalle.save()

#         ordenGuardada = OrdenDeCompra.objects.getOrden(newOrden.id)
#         return Response(OrdenDeCompraListSerializer(ordenGuardada).data)

#     def put(self, request, format=None):
#         serializer = self.serializer_class(data=self.request.data)
#         print(self.request.data)
#         serializer.is_valid(raise_exception=True)
#         import copy
#         orden = serializer.validated_data.copy()
#         print(orden)
#         productos = orden.pop('orden_detalle')

#         updateOrden = OrdenDeCompra.objects.get(id=self.request.data['id'])
#         updateOrdenSerializer = OrdenDeCompraUpdateSerializer(updateOrden,self.request.data)
#         updateOrdenSerializer.is_valid(raise_exception=True)
#         updateOrdenSerializer.save()

#         detalleBorrar = OrdenDeCompraDetalle.objects.filter(orden = self.request.data['id'])
#         detalleBorrar.delete()

#         for p in productos:
#             newOrdenDetalle = OrdenDeCompraDetalle(orden = updateOrden, **p)
#             newOrdenDetalle.save()

#         ordenGuardada = OrdenDeCompra.objects.getOrden(self.request.data['id'])
#         return Response(OrdenDeCompraListSerializer(ordenGuardada).data)

#     def delete(self, request, format=None):
#         pass