from django.contrib import admin
from .models import Proveedor, Producto

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'contacto', 'telefono', 'email']
    search_fields = ['nombre_empresa', 'contacto']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'id_proveedor']
    list_filter = ['categoria', 'id_proveedor']
    search_fields = ['nombre', 'descripcion']