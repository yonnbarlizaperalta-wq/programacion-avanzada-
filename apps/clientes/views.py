from django.shortcuts import render, redirect
from .models import Cliente, Inmueble
from .forms import InmuebleForm


# =========================
# INICIO
# =========================
def inicio(request):
    return render(request, 'inicio.html')


# =========================
# CLIENTES
# =========================
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {
        'clientes': clientes
    })


def formulario_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            documento=request.POST.get('documento'),
            telefono=request.POST.get('telefono'),
            tipo_inmueble=request.POST.get('tipo_inmueble'),
        )
        return redirect('lista_clientes')

    return render(request, 'clientes/formulario_cliente.html')


# =========================
# INMUEBLES
# =========================
def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/lista_inmuebles.html', {
        'inmuebles': inmuebles
    })


def formulario_inmueble(request):
    if request.method == 'POST':
        Inmueble.objects.create(
            tipo=request.POST.get('tipo'),
            direccion=request.POST.get('direccion'),
            ciudad=request.POST.get('ciudad'),
            precio=request.POST.get('precio'),
            habitaciones=request.POST.get('habitaciones'),
            banos=request.POST.get('banos'),
            area=request.POST.get('area'),
            parqueadero=request.POST.get('parqueadero') == 'True'
        )
        return redirect('lista_inmuebles')

    return render(request, 'inmuebles/formulario_inmueble.html')


def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm()

    return render(request, 'inmuebles/form.html', {'form': form})


# =========================
# ARRIENDOS
# =========================
def lista_arriendos(request):
    return render(request, 'arriendos/lista_arriendos.html')