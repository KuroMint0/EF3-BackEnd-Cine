from django.contrib import admin
from cine.models import Pelicula, Genero, Ticket
from django.utils.html import format_html

# Register your models here.

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'fecha_estreno', 'precio_formateado', 'estado', 'imagen')
    readonly_fields = ('imagen',)
    list_filter = ('genero',)
    search_field = ('nombre',)

    @admin.display(description='Imagen')
    def imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen.url)
        return "No hay imagen disponible"

    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return f"$ {obj.precio:,} CLP".replace(',', '.')

    @admin.display(boolean=True, description='En Cartelera')
    def estado(self, obj):
        return obj.is_active

    @admin.display(description='Fecha de Estreno')
    def fecha_estreno(self, obj):
        return obj.fecha_estreno.strftime('%d/%m/%Y')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'pelicula', 'nombre_cliente', 'cant_entradas', 'fecha_compra')
    list_filter = ('pelicula',)

    @admin.display(description='Código')
    def codigo(self, obj):
        return obj.id_ticket