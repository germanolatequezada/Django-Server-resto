from django.shortcuts import render, redirect
from restaurant.persistence.models import compra
from restaurant.views import login_view
import traceback


def index(request):

    if login_view.authorization_prov(request) == False:
        return redirect('/login/')
    print('index_compra')
    compra=[]
    message_success=None
    message_error=None
    try:
        compra = compra.objects.all()
        if request.method == 'POST':
            action = request.POST.get('action')
            print('action', action)            
            if action == 'create':
                return create_compra(request)
            if action == 'delete':
                return delete_compra(request)
            if action == 'update':
                return update_compra(request)
    except ValueError as e:
        message_success=None
        #errors=str(e).replace("'", "")
        #message_error=errors.split(',')
    except Exception as e:
        print(e)
        message_success=None
        message_error='Connection Error.'
    return render(request, 'compra/index.html', {'compra': compra, 
            'message_success': message_success, 'message_error': message_error})

def create_compra(request):
    print('create_compra')
    compra=[]
    message_success=None
    message_error=None
    try:
        nombre = request.POST.get('nombre')
        unidad = request.POST.get('unidad')
        compra = compra()
        compra.nombre = nombre
        compra.unidad = unidad
        compra.save()
        message_success='Registro Creado'
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al crear el registro.']
    compra = compra.objects.all()
    return render(request, 'compra/index.html', {'compra': compra, 
            'message_success': message_success, 'message_error': message_error})

def delete_compra(request):
    print('delete_compra')
    compra=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        compra = compra.objects.get(pk=id)
        compra.delete()
        message_success='Registro {0} Eliminado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al borrar el registro.']
    compra = compra.objects.all()
    return render(request, 'compra/index.html', {'compra': compra, 
            'message_success': message_success, 'message_error': message_error})

def update_compra(request):
    print('update_compra')
    compra=[]
    message_success=None
    message_error=None
    try:
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        unidad = request.POST.get('unidad')
        compra = compra.objects.get(pk=id)
        compra.nombre = nombre
        compra.unidad = unidad
        compra.save(force_update=True)
        message_success='Registro {0} Actualizado'.format(id)
        message_error=None
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al actualizar el registro']
    compra = compra.objects.all()
    return render(request, 'compra/index.html', {'compra': compra, 
            'message_success': message_success, 'message_error': message_error})                     