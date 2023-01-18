from django.urls import path, include
from .views import *


from django.conf import settings

app_name = 'apps.inventario'

urlpatterns = [
  
    path('setProductos/', SetProduc, name="productos"),
    # path('unidades/', UnidadApiView.as_view(), name="unidades"),
    # path('marcas/', MarcaApiView.as_view(), name="marcas"),
    # path('bodegas/', BodegaApiView.as_view(), name="bodegas"),
    # path('orden/', OrdenDeCompraApiView.as_view(), name="ordenes"),



    ]

