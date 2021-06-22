from django.urls import path
from .views import crearAeronave, registroAeronaves, index, galeria

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('registroAeronaves/', registroAeronaves, name="registroAeronaves"),
    path('crearAeronave', crearAeronave, name="crearAeronave" )
    
]