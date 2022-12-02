from django.shortcuts import render, redirect
from restaurant.persistence.models import Mesa
from restaurant.views import login_view
import traceback


def index(request):

    if login_view.authorization_prov(request) == False:
        return redirect('/login/')
    print('index_mesa')
    mesas=[]
    message_success=None
    message_error=None
    try:
        mesas = Mesa.objects.all()
        if request.method == 'POST':
            action = request.POST.get('action')
            print('action', action)            
            if action == 'create':
                return create_mesa(request)
            if action == 'delete':
                return delete_mesa(request)
            if action == 'update':
                return update_mesa(request)
    except ValueError as e:
        message_success=None
        #errors=str(e).replace("'", "")
        #message_error=errors.split(',')
    except Exception as e:
        print(e)
        message_success=None
        message_error='Connection Error.'
    return render(request, 'mesa/index.html', {'mesas': mesas, 
            'message_success': message_success, 'message_error': message_error})

def create_mesa(request):
    print('create_mesa')
    mesas=[]
    message_success=None
    message_error=None
    try:
        nombre = request.POST.get('nombre')
        capacidad = request.POST.get('capacidad')
        mesa = Mesa()
        mesa.nombre = nombre
        mesa.capacidad = capacidad
        mesa.save()
        message_success='Registro Creado'
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al crear el registro.']
    mesas = Mesa.objects.all()
    return render(request, 'mesa/index.html', {'mesas': mesas, 
            'message_success': message_success, 'message_error': message_error})

def delete_mesa(request):
    print('delete_mesa')
    mesas=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        mesa = Mesa.objects.get(pk=id)
        mesa.delete()
        message_success='Registro {0} Eliminado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al borrar el registro.']
    mesas = Mesa.objects.all()
    return render(request, 'mesa/index.html', {'mesas': mesas, 
            'message_success': message_success, 'message_error': message_error})

def update_mesa(request):
    print('update_mesa')
    mesas=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        capacidad = request.POST.get('capacidad')
        mesa = Mesa.objects.get(pk=id)
        mesa.nombre = nombre
        mesa.capacidad = capacidad
        mesa.save(force_update=True)
        message_success='Registro {0} Actualizado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al actualizar el registro']
    mesas = Mesa.objects.all()
    return render(request, 'mesa/index.html', {'mesas': mesas, 
            'message_success': message_success, 'message_error': message_error})                     