from django import forms
from django.forms import ModelForm
from .models import Aeronave

class AeronaveForm(ModelForm):
    
    class Meta:
        model = Aeronave
        fields = ['numeroSerie','marca','modelo','categoria']
        
        labels = {
            'numeroSerie': 'Digite numero de serie',
            'marca': 'Digite marca',
            'modelo': 'Digite modelo',
            'categoria': 'Seleccione Categoria'
        }
        
        widgets = {
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'numeroSerie',
                    'id': 'numeroSerie'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Marca',
                    'id': 'marca',
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Modelo',
                    'id': 'modelo'
                } 
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'categoria'
                } 
            ) 
        }