from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
import traceback

def index(request):
    # Si se encuentra logueado saltarse el formulario de login
    if authorization_prov(request):
        return redirect('/home/')

    if request.method == 'POST':
        try:
            username = request.POST.get('usuario')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home/')            
        except Exception as e:
            traceback.print_exc()
    return render(request, 'login.html')

# Autorización provisoria que no valida permisos, solo si esta autenticado
def authorization_prov(request):
    try:
        print('authorization | user -> ', request.user)

        if request.user != None and request.user.__str__() != 'AnonymousUser':
            return True
        else:
            print('Unauthorized')
            return False
    except Exception:
        return False

# Se debe usar esta autorización con permisos pero se deben crear los permisos previamente
def authorization(request, perm):
    print('authorization | user -> ', request.user)

    if request.user != None and request.user.__str__() != 'AnonymousUser':
        if request.user.has_perm(perm):
            print('Authorized')
            return True
        else:
            print('Forbidden')
            return False
    else:
        print('Unauthorized')
        return False    