from django.urls import path
from  .views import *

app_name = 'apps.configuracion'

urlpatterns = [
    path('prueba/', prueba, name="EMPRESA"),
    path('pdf/', obtenerPDF, name="EMPRESA"),
    path('status/', verificarStatus, name="EMPRESA"),
    path('repor/', getRepor, name="EMPRESA"),
    path('depa/', guardarDepa, name="EMPRESA"),
    path('muni/', guardarMuni, name="EMPRESA"),
    path('terceros/', guardarTercero, name="EMPRESA"),
    path('departamentos/',DepartamentosApiView.as_view()),
    path('municipios/',MunicipiosApiView.as_view()),
    path('formasDePago/',FormasApiView.as_view()),
    path('impuestos/',ImpuestosApiView.as_view()),
    path('retenciones/',RetencionesApiView.as_view()),
    path('empresa/',EmpresaApiView.as_view()),
    path('numeracion/',NumeracionApiView.as_view()),
    # path('terceros/',TercerosApiView.as_view()),
    path('vendedores/',VendedoresApiView.as_view()),
   
    
]