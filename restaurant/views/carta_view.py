from django.shortcuts import render
from restaurant.persistence.models import Plato
import random, traceback

def index(request):

    plato_tipico = buscar_azar_plato_por_tipo('plato tipico')
    sopa = buscar_azar_plato_por_tipo('sopa')
    ensalada = buscar_azar_plato_por_tipo('ensalada')
    helado = buscar_azar_plato_por_tipo('helado')
    mousse = buscar_azar_plato_por_tipo('mousse')
    pastel = buscar_azar_plato_por_tipo('pastel')
    cerveza = buscar_azar_plato_por_tipo('cerveza')
    bebida = buscar_azar_plato_por_tipo('bebida')
    jugo = buscar_azar_plato_por_tipo('jugo')

    #Renderizar carta
    return render(request, 'carta.html', {'plato_tipico': plato_tipico, 'sopa': sopa, 
            'ensalada': ensalada, 'helado': helado, 'mousse': mousse, 'pastel': pastel,
            'cerveza': cerveza, 'bebida': bebida, 'jugo': jugo})

def buscar_azar_plato_por_tipo(nombre_tipo):
    try:
        #Buscar platos por tipo en la base de datos, ordenados por nombre
        platos = Plato.objects.filter(tipo=nombre_tipo).order_by('nombre')
        #Seleccionar elemento de la lista al azar por indice
        indice = random.randint(0, len(platos)-1)
        #Buscar nombre del plato elegido de la lista obtenida de la base de datos
        nombre_plato = platos[indice].url_img
        return nombre_plato
    except Exception:
        traceback.print_exc()
        return None