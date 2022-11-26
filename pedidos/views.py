from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template


# Create your views here.

def Pedidos(request):
    
    fecha_actual=datetime.datetime.now()
    return render(request,"pedidos.html", {"dameFecha":fecha_actual})   

    #lkdhlkfsahlfea
