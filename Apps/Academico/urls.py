from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCursos/', views.registrarCursos),
    # path('edicionCursos/', views.edicionCursos),
    path('eliminarCursos/<area>', views.eliminarCursos),
]
