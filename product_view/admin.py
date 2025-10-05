from django.contrib import admin
from .models import Producto, Subcatalogo, Catalogo

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'creado')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('creado',)
    ordering = ('nombre',)

class SubcatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('productos',)
    ordering = ('nombre',)

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('subcatalogos',)
    ordering = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Subcatalogo, SubcatalogoAdmin)
admin.site.register(Catalogo, CatalogoAdmin)