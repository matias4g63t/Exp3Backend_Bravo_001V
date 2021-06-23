from django.urls import path
from .views import crearAeronave, registroAeronaves, index, galeria, form_modificar_aeronave, form_eliminar_aeronave

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('registroAeronaves/', registroAeronaves, name="registroAeronaves"),
    path('crearAeronave', crearAeronave, name="crearAeronave" ),
    path('form_modificar_aeronave/<id>', form_modificar_aeronave, name="form_modificar_aeronave"),
    path('form_eliminar_aeronave/<id>', form_eliminar_aeronave, name="form_eliminar_aeronave")
]