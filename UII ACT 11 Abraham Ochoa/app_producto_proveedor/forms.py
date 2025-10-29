from django import forms
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'contacto', 'telefono', 'email', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'foto_producto', 'categoria', 'precio', 'stock', 'id_proveedor']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }