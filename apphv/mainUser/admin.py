from django.contrib import admin
from .models import Usuarios

# Register your models here.

class UsuariosModelAdmin(admin.ModelAdmin):

    list_display = ("IdUsuario", "Nombre", "Apellido","Correo")

    search_fields = ('IdUsuario', 'GeneUsua', 'CeluUsua', 'TeleUsua')

    list_filter = ('IdUsuario', 'GeneUsua')


    class Meta:
        model = Usuarios
admin.site.register(Usuarios, UsuariosModelAdmin)


