from django.shortcuts import render, redirect
from restaurant.persistence.models import Mesa, Comanda, Cliente, AuthUser
from restaurant.persistence import comanda_custom_model
from restaurant.views import login_view
import traceback
from datetime import datetime

def index(request):

    if login_view.authorization_prov(request) == False:
        return redirect('/login/')
    print('index_comanda')
    mesas=[]
    message_success=None
    message_error=None
    try:
        mesas = Mesa.objects.all().order_by('nombre')
        clientes = Cliente.objects.all().order_by('nombre')
        usuarios = AuthUser.objects.all().order_by('username')
        if request.method == 'POST':
            action = request.POST.get('action')
            #print('action', action)            
            if action == 'create':
                return create_comanda(request)
            #if action == 'delete':
            #    return delete_mesa(request)
            #if action == 'update':
            #    return update_mesa(request)
    except ValueError as e:
        message_success=None
    except Exception as e:
        print(e)
        message_success=None
        message_error='Connection Error.'
    comandas = comanda_custom_model.find_all()
    return render(request, 'comanda/index.html', {'mesas': mesas, 
            'clientes':clientes, 'usuarios': usuarios, 'comandas': comandas,
            'message_success': message_success, 'message_error': message_error})

def create_comanda(request):
    print('create_comanda')
    comadas=[]
    message_success=None
    message_error=None
    try:         
        mesas = Mesa.objects.all().order_by('nombre')
        clientes = Cliente.objects.all().order_by('nombre')
        usuarios = AuthUser.objects.all().order_by('username')
        id_mesa = request.POST.get('mesa')
        id_usuario = request.POST.get('usuario')
        id_cliente = request.POST.get('cliente')
        if comanda_custom_model.find_by_mesa(id_mesa) == False:        
            comanda = Comanda()
            comanda.id_mesa = id_mesa
            comanda.id_usuario = id_usuario
            comanda.id_cliente = id_cliente
            comanda.fecha_inicio = datetime.now()
            comanda.save()
            message_success='Registro Creado'
            message_error=None
        else:
            message_success=None
            message_error=['Error al crear el registro. Mesa ya ocupada por una comanda.']            
    except Exception:
        traceback.print_exc()
        message_success=None
        message_error=['Error al crear el registro.']
    comandas = comanda_custom_model.find_all()
    return render(request, 'comanda/index.html', {'mesas': mesas, 
            'clientes':clientes, 'usuarios': usuarios, 'comandas': comandas,
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