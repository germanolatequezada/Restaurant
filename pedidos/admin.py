from django.contrib import admin

# Register your models here.

from Pedidos.models import Dim_cliente
from Pedidos.models import Dim_mesa


admin.site.register(Dim_cliente)
admin.site.register(Dim_mesa)