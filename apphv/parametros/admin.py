from django.contrib import admin
#Importamos cada una de las clases creadas en el archivo models.py:
from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr
from .models import Empleos

# Registrar tus modelos aqui.
# Agregamos la clase <<Model>>ModelaDMIN, para modificar la vista a cada uno de los mdelos importados:

class EtniaModelAdmin(admin.ModelAdmin):
     # Indicamos que columnas queremos ver(En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ["NombEtni"]
    # Indicamos que columna hacemos clic para editar:
    # list_display_links = ["NombEtni"]
    # Agregamos una barra de busqueda:
    search_fields = ["NombEtni"]
    # Podemos agregar un filtro:
    list_filter = ["NombEtni"]
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Etnia
admin.site.register(Etnia)


class TipoDocuModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver (En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ["NombTiDo"]
    # Indicamos que columna hacemos clic para editar:
    # list_display_links = [NombTiDo]
    # Agregamos una barra de busqueda:
    # search_fields = ["NombTiDo"]
    # Podemos agregar un filtro:
    # list_filter = ["NombTiDo"]
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu)

class EstaCivilModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver (En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ["NombEsCi"]
    # Indicamos que columna hacemos clic para editar:
    # list_display_links = [NombEsCi]
    # Agregamos una barra de busqueda:
    # search_fields = ["NombEsCi"]
    # Podemos agregar un filtro:
    # list_filter = ["NombEsCi"]
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = EstaCivil
admin.site.register(EstaCivil)

class TipoEstuModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver (En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ["NombTiEs"]
    # Indicamos que columna hacemos clic para editar:
    # list_display_links = [NombTiEs]
    # Agregamos una barra de busqueda:
    # search_fields = ["NombTiEs"]
    # Podemos agregar un filtro:
    # list_filter = ["NombTiEs"]
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = TipoEstu
admin.site.register(TipoEstu)

class TipoLogrModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver (En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ["NombTiLo"]
    # Indicamos que columna hacemos clic para editar:
    # list_display_links = [NombTiLo]
    # Agregamos una barra de busqueda:
    # search_fields = ["NombTiLo"]
    # Podemos agregar un filtro:
    # list_filter = ["NombTiLo"]
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = TipoLogr
admin.site.register(TipoLogr)

class EmpleoModelAdmin(admin.ModelAdmin):
    # Indicamos que columnas queremos ver (En este caso solo mostramos el nombre ya que no tenemos otras):
    list_display = ('__str__','NombCarg', 'EsCargo')
    # Indicamos que columna hacemos clic para editar:
    list_display_links = ('NombCarg',)
    # Agregamos una barra de busqueda:
    search_fields = ('NombCarg',)
    # Podemos agregar un filtro:
    list_filter = ('EsCargo',)
    # Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Empleos
admin.site.register(Empleos)


