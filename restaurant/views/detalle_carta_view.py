from django.shortcuts import render
from restaurant.persistence.models import Plato, ComandaDetalle
from restaurant.persistence import comanda_custom_model
from restaurant.persistence import comanda_detalle_custom_model
import random, traceback

def index(request):
    tipo = ''
    platos = []
    comandas = [] 
    try:
        if(request.method == 'GET'):
            tipo = request.GET.get('tipo')
            platos = Plato.objects.filter(tipo=tipo).order_by('nombre')
        if (request.method == 'POST'):
            comanda = request.POST.get('comanda')
            plato = request.POST.get('plato')
            cantidad = request.POST.get('cantidad')
            precio = request.POST.get('precio')
            tipo = request.POST.get('tipo')
            platos = Plato.objects.filter(tipo=tipo).order_by('nombre')
            comanda_detalle = ComandaDetalle()
            comanda_detalle.id_comanda = comanda
            comanda_detalle.id_plato = plato
            comanda_detalle.cantidad = cantidad
            comanda_detalle.precio = int(precio)/int(cantidad)
            comanda_detalle_custom_model.save_comanda_detalle(comanda_detalle)
        comandas = comanda_custom_model.find_all()
    except Exception:
        traceback.print_exc()
    return render(request, 'detalle_carta.html', {'tipo': tipo, 'platos': platos, 'comandas': comandas })