
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, cod_usuario, usuario, password=None):
        now = timezone.now()
        pass

class Usuario(AbstractBaseUser):
    cod_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=30,default='')
    apellido = models.CharField(max_length=30,default='')
    correo = models.CharField(max_length=40,default='')
    password = models.CharField(max_length=30,)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'

    def check_password(self, password ):

        return self.password == password 

    def __str__(self):
        return self.usuario


class Cuenta(models.Model):
    cod_cuenta = models.AutoField(primary_key=True)
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    saldo = models.IntegerField()

    def __str__(self):
        return str(self.cod_cuenta)


class TipoMaterial(models.Model):
    cod_tipo_material = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre


class Material(models.Model):
    cod_material = models.AutoField(primary_key=True)
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cod_tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='static/img/')
    estado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cod_material)


class TipoTransaccion(models.Model):
    cod_tipo_tra = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Transaccion(models.Model):
    cod_tra = models.AutoField(primary_key=True)
    cod_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    cod_tipo_tra = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return str(self.cod_tra)
