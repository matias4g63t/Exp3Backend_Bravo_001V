from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def registroAeronaves(request):
    return render(request, 'registroAeronaves.html')