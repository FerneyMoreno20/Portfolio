from django.db import models
# Create your models here.
# los modelos son una clase que devuelve un objeto
# por lo que crearemos una clase con el nombre de la entidad o coleccion y definiremos los atributos

# Clase para el modelo Etnia, esta clase se encargara:
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50)

    # ya creada la clase, retornamos el objeto NombEtni, o nombre de Etnia
    def __str__(self):
        return self.NombEtni

# Agregamos las otras clases del modulo:

# Clase para el modelo TipoDocu:
class TipoDocu(models.Model):
    NombTiDo = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombTiDo

# Clase para el modelo EstaCivil o estado civil
class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombEsCi

# Clase para el modelo  TipoEstu o clasificacion de los estudios :
class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombTiEs

# Clase para el modelo TipoLogr o Tipos de Logro:
class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombTiLo

# Clase para cargos:
class Empleos(models.Model):

    DomiCarg = models.CharField(max_length = 1, default="", verbose_name="Dominio")  
    ClasCarg = models.CharField(max_length = 2, default="", verbose_name="Clase") 
    OrdeCarg = models.CharField(max_length = 3, default="", verbose_name="Orden")
    GeneCarg = models.CharField(max_length = 4, default="", verbose_name="Genero")
    NombCarg = models.CharField(max_length = 250, default="", verbose_name="Nombre de Cargo")
    EsCargo = models.CharField(max_length = 20, default="", verbose_name="Es Cargo")

    class Meta:
        verbose_name = "Cargos"
        verbose_name_plural = "Empleos y Cargos"

    def __str__(self):
        return self.NombCarg