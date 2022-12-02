
from restaurant.persistence.models import Mesa, Comanda, Cliente, AuthUser
import traceback
from datetime import datetime


def find_all():
    comandas = Comanda.objects.filter(fecha_fin__isnull=True).order_by('-fecha_inicio')
    comandas_json = []
    for comanda in comandas:
        id = comanda.id
        mesa = Mesa.objects.get(pk=comanda.id_mesa)
        usuario = AuthUser.objects.get(pk=comanda.id_usuario)
        cliente = Cliente.objects.get(pk=comanda.id_cliente)
        comanda_json = {
            'id': id,
            'mesa': mesa.nombre,
            'usuario': usuario.username,
            'cliente': cliente.nombre + ' ' + cliente.apellido_paterno,
            'fecha_inicio': comanda.fecha_inicio,
            'fecha_fin': comanda.fecha_fin
        }
        comandas_json.append(comanda_json)
    return comandas_json

def find_by_mesa(id_mesa):
    comandas = comandas = Comanda.objects.filter(fecha_fin__isnull=True).order_by('-fecha_inicio')
    for comanda in comandas:
        if int(comanda.id_mesa) == int(id_mesa):
            return True
    return False