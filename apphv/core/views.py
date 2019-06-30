from django.shortcuts import render, HttpResponse,redirect
# Create your views here.

from  django.core.exceptions import ObjectDoesNotExist

from django.urls import reverse
from .forms import ContactForm
from mainUser.forms import DatosP
from mainUser.models import Usuarios

from .forms import ContactForm

def indexcore(request):
        
    FormContact = ContactForm()

    if request.method == "POST":

        FormContact = ContactForm(data=request.POST)

        if FormContact.is_valid():

            email = request.POST.get('email', '')
            tipom = request.POST.get('tipom', '')
            nombre = request.POST.get('nombre', '')
            msj = request.POST.get('msj', '')

            FormContact.save()
            return redirect('nosotros')

    return render(request, 'core/index.html', {'formulario': FormContact})



def nosotros(request):
    return render(request, 'core/nosotros.html')

def login(request):
    return render(request, 'core/login.html')
    
def registrar(request):
    return render(request, 'core/registrar.html')

def recover(request):
    return render(request, 'core/recuperarContraseña.html')

def newpass(request):
    return render(request, 'core/nuevaContraseña.html')



def crearU(request):
    if request.method == 'POST':
        datos_form = DatosP(request.POST)
        if datos_form.is_valid():
            datos_form.save()
            return redirect('listarU')
     
    else:
        datos_form = DatosP()
    return render(request, 'core/crearU.html',{'datos_form': datos_form})

def listarU(request):
    usuarios = Usuarios.objects.filter(EstaUsua = True)
    return render(request,'core/perfilU1.html',{'usuarios': usuarios})
  

def editarU(request,IdUsuario):
    datos_form = None
    error = None
    try:
        usuario = Usuarios.objects.get(IdUsuario = IdUsuario)
        if request.method == 'GET':
            datos_form = DatosP(instance = usuario)
        else:
            datos_form = DatosP(request.POST, instance = usuario)
            if datos_form.is_valid():  
                datos_form.save()
            return redirect('listarU')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'core/editUser.html',{'datos_form': datos_form,'error': error})

def eliminarU(request,IdUsuario):
     usuario = Usuarios.objects.get(IdUsuario = IdUsuario)
     usuario.EstaUsua = False
     usuario.save()
     return redirect('listarU')


