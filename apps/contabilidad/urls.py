from django.urls import path
from  .views import *

app_name = 'apps.contabilidad'

urlpatterns = [
    # path('depa/', guardarDepa, name="EMPRESA"),
    path('puc/', PucApiView.as_view(), name="puc"),
    
]