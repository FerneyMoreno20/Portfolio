from django.db import models
from django import forms 
from parametros.models import TipoDocu, EstaCivil, Etnia, Empleos,TipoLogr, TipoEstu





# Create your models here.
class Usuarios(models.Model):
    IdUsuario = models.CharField(primary_key=True,max_length = 50, verbose_name = "No. Identificación", default="")
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete=models.CASCADE, verbose_name="Tipo de documento",null=True)
    idEstaCivil = models.ForeignKey(EstaCivil, default="", on_delete=models.CASCADE, verbose_name="Estado civil",null=True)
    idEtnias = models.ForeignKey(Etnia, default="", on_delete=models.CASCADE, verbose_name="Etnias",null=True)
    Nombre = models.CharField(max_length =200, default = "", verbose_name = "Nombre")
    Apellido = models.CharField(max_length =200, default = "", verbose_name = "Apellido")
    Correo = models.CharField(max_length =250, default = "", verbose_name = "Correo")
    ImagUsua = models.ImageField(verbose_name = "Foto de Perfil", upload_to = "perfiles/img")
    PerfilPro = models.CharField(max_length = 250,default="Candidato...", verbose_name="Perfil Profesional")
    GeneUsua = models.CharField(max_length = 1, verbose_name = "Género")
    TeleUsua = models.CharField(max_length = 20, default = "", verbose_name = "Teléfono")
    CeluUsua = models.CharField(max_length =20, default = "", verbose_name = "Celular")
    DireUsua = models.CharField(max_length =50, default = "", verbose_name = "Dirección Postal")
    RegiUsua = models.DateField(auto_now_add = False,  verbose_name = "Registrado el: " ,null=True)
    EstaUsua = models.BooleanField(default = "Activo", verbose_name = "Estado")
    TipoEstu = models.ForeignKey(TipoEstu, on_delete = models.CASCADE,default="",verbose_name = "Tipo de educación",null=True)
    Instituto = models.CharField(max_length = 30, verbose_name = "Inistitución o Academia",null=True)
    TituloEst = models.CharField(max_length = 250, verbose_name = "Titulo de estudio",null=True)
    NombTiLo = models.ForeignKey(TipoLogr, on_delete = models.CASCADE, verbose_name="Tipo de Logro",null=True)
    FechLogr = models.DateField(auto_now_add = False, verbose_name = "Fecha de culminación de logro",null=True)
    NombLogr = models.CharField(max_length = 100, verbose_name = "Logro o Distinción",null=True)
    DescLogr = models.CharField( max_length = 250, verbose_name = "Descripción o caracteristicas del logro",null=True)
    CargExpe = models.ForeignKey(Empleos, on_delete=models.CASCADE, verbose_name="Cargo Ocupado", null=True)
    EmprExpe = models.CharField(max_length = 150, verbose_name = "Empresa",null=True)
    FuncionE = models.CharField(max_length = 250,verbose_name = "Funciones desempeñadas",null=True)
    LogrExpe = models.CharField(max_length = 250,verbose_name = "Logros Alcanzados",null=True)
    NombHabil = models.CharField(max_length = 100, default="", verbose_name = "Habilidad",null=True)
    NiveHabil = models.CharField(max_length = 20, default="", verbose_name = "Nivel de Habilidad ",null=True)
   

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    

    def __str__(self):
        return self.IdUsuario


