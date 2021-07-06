from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, Productoform

# Create your views here.

def home(request):
        productos = Producto.objects.all()
        data = {
                'productos': productos

        }
        return render(request, 'app/home.html', data)

def galeria(request):
        return render(request, 'app/galeria.html')

def contacto(request):
        data ={
                'form': ContactoForm()
        }
        if request.method =='POST':
                formulario = ContactoForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"]= "contacto guardado"
                else:
                        data["form"] = formulario
        return render(request, 'app/contacto.html',data)
def agregar_producto(request):
        data= {
                'form': Productoform()
        }
        if request.method =='POST':
                formulario = Productoform(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"] = "guardado correctamente"
                else:
                 data["form"] = formulario
        return render (request, 'app/producto/agregar.html', data)

def modificar_producto(request, id):
        producto = get_object_or_404(Producto, id=id)

        data = {
                'form' ProductoForm(instance=producto)
        }
        if request.method =='POST':
                        formulario = Productoform(data=request.POST, files=request.FILES)
                        if formulario.is_valid():
                                formulario.save()
                                data["mensaje"] = "guardado correctamente"
                        else:
                        data["form"] = formulario
        
        return render (request, 'app/producto/modificar.html', data)