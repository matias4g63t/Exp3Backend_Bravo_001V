from django.shortcuts import redirect, render
from .models import Categoria, Aeronave
from .forms import AeronaveForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def registroAeronaves(request):
    aeronaves = Aeronave.objects.all()        #similar a un select de BD
    return render(request, 'registroAeronaves.html',context={'datos': aeronaves})

def crearAeronave(request):
    if request.method=='POST':
        aeronave = AeronaveForm(request.POST)
        if aeronave.is_valid():
            aeronave.save()
            return redirect('registroAeronaves')
    else:
        aeronave=AeronaveForm() 
    return render(request, 'app_dron/form_crearAeronave.html',{'aeronave': aeronave})

def Ver(request):
    aeronaves = Aeronave.objects.all()
    return render(request,'registroAeronaves', context={'aeronaves':aeronaves})

def form_modificar_aeronave(request,id):
    aeronave = Aeronave.objects.get(numeroSerie =id)
    
    datos={
        'form': AeronaveForm(instance=aeronave)
    }
    if request.method == "POST":
        formulario = AeronaveForm(data=request.POST, instance = aeronave)
        if formulario.is_valid:
            formulario.save()
            return redirect('registroAeronaves')
    return render(request, 'app_dron/form_modificar_aeronave.html', datos)