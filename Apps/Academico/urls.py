from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCursos/', views.registrarCursos),
    path('edicionCursos/<area>', views.edicionCursos),
    path('editarArea/', views.editarArea),
    path('eliminarCursos/<area>', views.eliminarCursos),
]
