from restaurant.persistence.models import ComandaDetalle, Comanda, Mesa, Plato
import traceback

def save_comanda_detalle(comanda_detalle):
    detalles_comandas = []
    try:
        try:
            detalles_comandas = ComandaDetalle.objects.filter(id_comanda=comanda_detalle.id_comanda)
        except Exception:
            traceback.print_exc()
        det_comanda = None
        for detalle in detalles_comandas:
            if int(detalle.id_plato) == int(comanda_detalle.id_plato):
                det_comanda = detalle
        if det_comanda == None:
            comanda_detalle.save()
        else:
            det_comanda.cantidad = int(det_comanda.cantidad) + int(comanda_detalle.cantidad)
            det_comanda.save(force_update=True)
    except Exception:
        traceback.print_exc()

def find_by_mesa(id_mesa):
    detalles_comandas_json = []
    try:
        #Buscar comanda abierta por id mesa
        comanda = Comanda.objects.filter(id_mesa=id_mesa, fecha_fin__isnull=True)
        id = None
        usuario = None
        for c in comanda:
            id = c.id
            usuario = c.id_usuario
        detalles_comandas = ComandaDetalle.objects.filter(id_comanda=id)
        mesa = Mesa.objects.get(pk=id_mesa)
        for detalle in detalles_comandas:
            
            plato = Plato.objects.get(pk=detalle.id_plato)
            detalle_json = {
                'mesa': mesa.nombre,
                'plato': plato.nombre,
                'plato_img': plato.url_img,
                'precio': detalle.precio,
                'cantidad': detalle.cantidad,
                'total': detalle.precio*detalle.cantidad,
                'comanda': id,
                'usuario': usuario
            }
            detalles_comandas_json.append(detalle_json)
    except Exception:
        traceback.print_exc()
    return detalles_comandas_json        