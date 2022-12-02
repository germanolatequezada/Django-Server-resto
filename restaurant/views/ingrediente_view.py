from django.shortcuts import render, redirect
from restaurant.persistence.models import Ingrediente
from restaurant.views import login_view
import traceback


def index(request):

    if login_view.authorization_prov(request) == False:
        return redirect('/login/')
    print('index_ingrediente')
    ingredientes=[]
    message_success=None
    message_error=None
    try:
        ingredientes = Ingrediente.objects.all()
        if request.method == 'POST':
            action = request.POST.get('action')
            print('action', action)            
            if action == 'create':
                return create_ingrediente(request)
            if action == 'delete':
                return delete_ingrediente(request)
            if action == 'update':
                return update_ingrediente(request)
    except ValueError as e:
        message_success=None
        #errors=str(e).replace("'", "")
        #message_error=errors.split(',')
    except Exception as e:
        print(e)
        message_success=None
        message_error='Connection Error.'
    return render(request, 'ingrediente/index.html', {'ingredientes': ingredientes, 
            'message_success': message_success, 'message_error': message_error})

def create_ingrediente(request):
    print('create_ingrediente')
    ingredientes=[]
    message_success=None
    message_error=None
    try:
        nombre = request.POST.get('nombre')
        unidad = request.POST.get('unidad')
        ingrediente = Ingrediente()
        ingrediente.nombre = nombre
        ingrediente.unidad = unidad
        ingrediente.save()
        message_success='Registro Creado'
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al crear el registro.']
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente/index.html', {'ingredientes': ingredientes, 
            'message_success': message_success, 'message_error': message_error})

def delete_ingrediente(request):
    print('delete_ingrediente')
    ingredientes=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        ingrediente = Ingrediente.objects.get(pk=id)
        ingrediente.delete()
        message_success='Registro {0} Eliminado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al borrar el registro.']
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente/index.html', {'ingredientes': ingredientes, 
            'message_success': message_success, 'message_error': message_error})

def update_ingrediente(request):
    print('update_ingrediente')
    ingredientes=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        unidad = request.POST.get('unidad')
        ingrediente = Ingrediente.objects.get(pk=id)
        ingrediente.nombre = nombre
        ingrediente.unidad = unidad
        ingrediente.save(force_update=True)
        message_success='Registro {0} Actualizado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al actualizar el registro']
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente/index.html', {'ingredientes': ingredientes, 
            'message_success': message_success, 'message_error': message_error})                     