from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendario/', views.calendario, name='calendario'),
    path('staff/', views.ver_equipo, name='ver_equipo'),
    path('staff/modificar/', views.modificar_equipo, name='modificar_equipo'),
    path('staff/sumar/', views.sumar_integrante, name='sumar_integrante'),
    path('inventario/', views.ver_ingredientes, name='ver_ingredientes'),
    path('inventario/modificar/', views.modificar_lista, name='modificar_lista'),
    path('inventario/sumar/', views.sumar_ingrediente, name='sumar_ingrediente'),
    path('cuentas/modificar/', views.modificar_gastos, name='modificar_gastos'),
    path('cuentas/sumar/', views.sumar_gasto, name='sumar_gasto'),
    path('menu/modificar/', views.modificar_carta, name='modificar_carta'),
    path('menu/sumar/', views.sumar_plato, name='sumar_plato'),
]
