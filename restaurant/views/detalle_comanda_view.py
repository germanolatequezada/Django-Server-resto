from django.shortcuts import render, redirect
from restaurant.persistence.models import Mesa, Comanda, Cliente, AuthUser
from restaurant.persistence import comanda_detalle_custom_model
from restaurant.views import login_view
import traceback

def index(request):

    if login_view.authorization_prov(request) == False:
        return redirect('/login/')
    print('index_comanda')
    detalles_comandas=[]
    message_success=None
    message_error=None
    total = 0
    id_comanda = None
    id_usuario = None
    try:
        mesas = Mesa.objects.all().order_by('nombre')
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'find':
                id_mesa = request.POST.get('mesa')
                detalles_comandas = comanda_detalle_custom_model.find_by_mesa(id_mesa)
                for detalle in detalles_comandas:
                    id_comanda = detalle['comanda']
                    id_usuario = detalle['usuario']
                    total = total + detalle['total']
    except ValueError as e:
        message_success=None
    except Exception as e:
        print(e)
        message_success=None
        message_error='Connection Error.'
    return render(request, 'detalle_comanda/index.html', {'mesas': mesas, 'detalles_comandas': detalles_comandas, 
            'total': total, 'id_comanda': id_comanda, 'id_usuario': id_usuario,
            'message_success': message_success, 'message_error': message_error})
