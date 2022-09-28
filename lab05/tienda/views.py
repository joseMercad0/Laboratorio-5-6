from multiprocessing import context
from django.shortcuts import render

from .models import Producto

def index(request):
    lista_producto = Producto.objects.all()
    print(lista_producto)
    context= {
        'productos': lista_producto
    }
    return render(request, 'index.html',context)
# Create your views here.
