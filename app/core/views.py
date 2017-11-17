from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import *
from app.core.forms import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from .models import *

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def borrar_cuenta(request):
    if request.method == 'GET':
        return get_borrar_cuenta_form(request)
    elif request.method == 'POST':
        return handle_borrar_cuenta_form(request)

def get_borrar_cuenta_form(request):
    user = request.user
    user.refresh_from_db()
    form = BorrarCuenta()
    return render(request, 'borrar-cuenta.html', {'form': form, 'user': user})

def handle_borrar_cuenta_form(request):
    username = request.user.username
    form = BorrarCuenta(request.POST)
    if form.is_valid():
        rem = User.objects.get(username=username)
        if rem is not None:
            rem.delete()
        else:
            return None
        return redirect('home')
    else:
        return render(request, 'borrar-cuenta.html', {'form': form})
@login_required

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})

def modificar_desocupado(request):
    args = {}
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ModificarDesocupado(request.POST, instance=user.desocupado)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ModificarDesocupado(instance=user.desocupado)

    args['form'] = form
    return render(request, 'modificar-desocupado.html', args)

