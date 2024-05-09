# Definir las rutas 
from django.urls import path
from mantenimientos.api.views import PersonajeAPIView
urlpatterns = [
    path('personajes/', PersonajeAPIView.as_view(), name='personajes' ),
    path('personajes/<int:pk>/', PersonajeAPIView.as_view(), name='personaje_detalle' )
]
