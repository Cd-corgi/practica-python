from django.urls import path, include
from .views import *


from django.conf import settings

app_name = 'apps.stock'

urlpatterns = [
  
    path('setProductos/', SetProduc, name="productos"),
    path('setInventario/', SetInven, name="productos"),
    path('getProductos/', getProductos, name="getProductos"),
    path('ordenCompra/', ordenCompra, name="ordenCompra"),
    path('ingreso/', ingresos, name="ingresos")


    # path('unidades/', UnidadApiView.as_view(), name="unidades"),
    # path('marcas/', MarcaApiView.as_view(), name="marcas"),
    # path('bodegas/', BodegaApiView.as_view(), name="bodegas"),
    # path('orden/', OrdenDeCompraApiView.as_view(), name="ordenes"),



    ]

