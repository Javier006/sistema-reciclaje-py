from django.urls import path
from App import views

urlpatterns = [
    path('Login/',views.Login, name='login'),
    path('Materiales/', views.Materiales),
    path('Sucursales/', views.Sucursales),
    path('Recompensas/', views.Recompensas),
    path('Mi-Cuenta/', views.MiCuenta),
    path('Nosotros/', views.QuienesSomos),
    path('Contacto/', views.Contacto),
    path('Registrar/', views.Registrar, name='registrar'),
    path('AprendeReciclar/', views.AprendeReciclar),
    #CRUD
    path('eliminar/<int:pk>', views.eliminarMaterial),
    #ADMINISTRADOR
    path('administrador/', views.administrador, name='administrador'),
]