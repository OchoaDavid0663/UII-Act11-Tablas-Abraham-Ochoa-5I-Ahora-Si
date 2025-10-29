from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=200, help_text="Nombre de la empresa proveedora")
    contacto = models.CharField(max_length=100, help_text="Persona de contacto")
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto_producto = models.ImageField(upload_to='img_productos/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"