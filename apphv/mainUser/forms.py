from django import forms 
from .models import Usuarios

class DatosP(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['IdUsuario','idTipoDocu','Nombre','Apellido','Correo','DireUsua','TeleUsua','CeluUsua','idEtnias','idEstaCivil','GeneUsua',
        'RegiUsua','EstaUsua','PerfilPro','TipoEstu','Instituto','TituloEst','NombTiLo','FechLogr','NombLogr','CargExpe','EmprExpe','FuncionE',
        'LogrExpe','DescLogr','NombHabil','NiveHabil']
        widgets = {
            'IdUsuario' : forms.TextInput(attrs={'class':'form-control'}),
            'idTipoDocu': forms.Select(attrs={'class':'form-control'}),
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'Correo' : forms.TextInput(attrs={'class':'form-control'}),
            'DireUsua' : forms.TextInput(attrs={'class':'form-control'}),
            'TeleUsua' : forms.TextInput(attrs={'class':'form-control'}),
            'CeluUsua' : forms.TextInput(attrs={'class':'form-control'}),
            'idEtnias' : forms.Select(attrs={'class':'form-control'}),
            'idEstaCivil' : forms.Select(attrs={'class':'form-control'}),
            'GeneUsua' : forms.TextInput(attrs={'class':'form-control'}),
            'RegiUsua' : forms.DateInput(attrs={'class':'form-control'}),
            'EstaUsua' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'PerfilPro' : forms.Textarea(attrs={'class':'form-control'}),
            'TipoEstu' : forms.Select(attrs={'class':'form-control'}),
            'Instituto' : forms.TextInput(attrs={'class':'form-control'}),
            'TituloEst' : forms.TextInput(attrs={'class':'form-control'}),
            'NombTiLo' : forms.Select(attrs={'class':'form-control'}),
            'FechLogr' : forms.TextInput(attrs={'class':'form-control'}),
            'NombLogr' : forms.TextInput(attrs={'class':'form-control'}),
            'CargExpe' : forms.Select(attrs={'class':'form-control'}),
            'EmprExpe' : forms.TextInput(attrs={'class':'form-control'}),
            'FuncionE' : forms.Textarea(attrs={'class':'form-control'}),
            'LogrExpe' : forms.Textarea(attrs={'class':'form-control'}),
            'DescLogr' : forms.Textarea(attrs={'class':'form-control'}),
            'NombHabil' : forms.TextInput(attrs={'class':'form-control'}),
            'NiveHabil' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
        