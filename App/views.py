from django.shortcuts import render, redirect
from App.models import Material,TipoMaterial,Usuario,Cuenta,TipoTransaccion,Transaccion
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from googleapiclient.discovery import build
from datetime import datetime
import os, requests

# Create your views here.



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        Usuario = authenticate(request, username=username, password=password)
        if Usuario is not None:
            login(request, Usuario)
            pk = Usuario.cod_usuario
            return redirect('../Materiales/?pk='+str(pk))
        else:
            # ERROR CONTRASEÑA O USUARIO
            return render(request, 'App/Login.html')
    else:
        #ERROR NINGUN CAMPO INGRESADO
        return render(request,'App/Login.html')   


def Materiales(request):
    pk = request.GET.get('pk')
    material = Material.objects.filter(cod_usuario_id=pk)
    tipomaterial = TipoMaterial.objects.all()
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    # Se Filtra el usuario por PK y tomando los materiales por sus valores y sumarlos
    
    saldo = Material.objects.filter(cod_usuario_id=pk, estado=True).aggregate(saldo=Sum('cod_tipo_material__valor'))['saldo']

    if saldo is None or saldo == 0:
        saldo = 0

    # Obtener la cuenta existente si existe
    cuenta = Cuenta.objects.filter(cod_usuario_id=pk).first()  

    if cuenta:
        # Actualizar el saldo de la cuenta existente
        cuenta.saldo = saldo
        cuenta.save()
    else:
        # Crear una nueva cuenta
        cuenta = Cuenta(saldo=saldo, cod_usuario_id=pk)
        cuenta.save()


    # CRUD - AGREGAR MATERIAL
    if request.method == 'POST':
        cod_tipo_material_id = request.POST['material']
        if request.FILES.get('foto', False):
            foto = request.FILES['foto']
            # Obtener el ID del usuario desde pk
            cod_usuario_id = pk
    
            # Crear y guardar el objeto Material
            p = Material(foto=foto, cod_tipo_material_id=cod_tipo_material_id, cod_usuario_id=cod_usuario_id)
            p.save()
                     
            return redirect('../Materiales/?pk='+str(pk))
        
    return render(request, 'App/Materiales.html', {'material': material, 'tipomaterial': tipomaterial , 'usuario' : usuario, 'cuenta' : cuenta})




def eliminarMaterial(request, pk):
    try:
        material = Material.objects.get(cod_material=pk)
        pk1 = material.cod_usuario_id
        if material.foto:
            # Eliminar archivo de la foto
            os.remove(material.foto.path)
        
        material.delete()

        return redirect('../Materiales/?pk=' + str(pk1))
    
    except Material.DoesNotExist:
        return redirect('../Materiales/')

@csrf_exempt
def administrador(request):
    materiales = Material.objects.all().order_by('cod_usuario_id')
    if request.method == 'POST':
        material_id = request.POST.get('material_id')
        material = Material.objects.get(cod_material=material_id)
        material.estado = not material.estado
        material.save()
        return redirect('../administrador/')

    return render(request, 'App/Administrador.html', {'materiales': materiales})


def Sucursales(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta,cod_usuario_id=pk)
    return render(request, 'App/Sucursales.html',{'usuario' : usuario,'cuenta' : cuenta})

def Recompensas(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta,cod_usuario_id=pk)
    tipotransaccion = TipoTransaccion.objects.all()

    
    if request.method == 'POST':
        transaccion = request.POST['tipotransaccion']
        monto = request.POST['saldo']
        c = Cuenta.objects.get(cod_usuario_id=pk)
        fecha = datetime.now()
        z = c.cod_cuenta
        t = Transaccion(cod_tipo_tra_id=transaccion,cod_cuenta_id=z,monto=monto,fecha=fecha)
        t.save()

        cuenta.saldo = cuenta.saldo - int(monto)
        cuenta.save()

        return redirect('../Recompensas/?pk='+ str(pk) +'&success=true')


    return render(request, 'App/Recompensas.html',{'usuario' : usuario,'cuenta' : cuenta,'tipotransaccion' : tipotransaccion})

def MiCuenta(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta,cod_usuario_id=pk)
    return render(request, 'App/MiCuenta.html',{'usuario' : usuario,'cuenta' : cuenta})

def QuienesSomos(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta,cod_usuario_id=pk)
    return render(request, 'App/QuienesSomos.html',{'usuario' : usuario,'cuenta' : cuenta})

def Contacto(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta,cod_usuario_id=pk)
    return render(request, 'App/Contacto.html',{'usuario' : usuario,'cuenta' : cuenta})

def Registrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        password = request.POST['password']

        r = Usuario(usuario=username,password=password,apellido=apellido,correo=correo,nombre=nombre)
        r.save()

        return redirect('../Login/')

    return render(request,'App/Registrar.html')


def AprendeReciclar(request):
    pk = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, cod_usuario=pk)
    cuenta = get_object_or_404(Cuenta, cod_usuario_id=pk)

    # API VIDEOS

    API_KEY2 = 'AIzaSyB3CJtbLWJob6j5WQ68sDI4x8OgmZIG2Ec'
    youtube_service = build('youtube', 'v3', developerKey=API_KEY2)

    papel_search_response = youtube_service.search().list(
        q='¿Cómo reciclar? - Guía completa de reciclaje - Algohayquehacer',
        part='snippet',
        type='video',
        maxResults=3
    ).execute()

    # Obtener los datos de los videos de reciclaje de papel
    videos_papel = papel_search_response['items']


    # API NOTICIAS
    API_KEY = '443d50d0dc8a4172b605015063f6690e'
    url = f'https://newsapi.org/v2/everything?q=reciclaje&apiKey={API_KEY}'
    response = requests.get(url)
    noticias = response.json()


    if noticias['status'] == 'ok':
        articles = [article for article in noticias['articles'] if 'reciclos' not in article['title'].lower()]
        return render(request, 'App/AprendeReciclar.html', {'articles': articles,'usuario': usuario, 'cuenta': cuenta,'videos_papel': videos_papel})


    return render(request, 'App/AprendeReciclar.html', {'usuario': usuario, 'cuenta': cuenta, 'videos_papel': videos_papel})

