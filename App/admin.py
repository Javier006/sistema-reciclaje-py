from django.contrib import admin
from .models import Usuario,TipoMaterial,Cuenta,Material,TipoTransaccion,Transaccion

# Register your models here.


admin.site.register(Usuario)

admin.site.register(TipoMaterial)

admin.site.register(Cuenta)

admin.site.register(Material)

admin.site.register(TipoTransaccion)

admin.site.register(Transaccion)