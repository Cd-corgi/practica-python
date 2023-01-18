from django.shortcuts import render

from .models import *
from .serializers import *
from apps.users.models import User
from apps.configuracion.models import Impuestos

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

        celdas = hoja['A2':'R3246']

        lista_productos = []

        lista_p = []
        for fila in celdas:
            producto = [celda.value for celda in fila]
            lista_productos.append(producto)

        
        usuario = User.objects.get(id=1)
        imp = Impuestos.objects.get(id=1)
        for p in lista_productos:
            tipo = tipoProducto.objects.get(id = p[5])
            product = ProductosSumi()
           
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