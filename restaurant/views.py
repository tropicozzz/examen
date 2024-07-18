from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calendario(request):
    return render(request, 'calendario.html')

def ver_equipo(request):
    return render(request, 'staff.html')

def modificar_equipo(request):
    return render(request, 'modificar_equipo.html')

def sumar_integrante(request):
    return render(request, 'sumar_integrante.html')

def ver_ingredientes(request):
    return render(request, 'inventario.html')

def modificar_lista(request):
    return render(request, 'modificar_lista.html')

def sumar_ingrediente(request):
    return render(request, 'sumar_ingrediente.html')

def modificar_gastos(request):
    return render(request, 'modificar_gastos.html')

def sumar_gasto(request):
    return render(request, 'sumar_gasto.html')

def modificar_carta(request):
    return render(request, 'modificar_carta.html')

def sumar_plato(request):
    return render(request, 'sumar_plato.html')
