function add_comanda(id) {
    cantidad = parseInt(document.getElementById("txt-cantidad-"+id).value)
    cantidad = cantidad + 1
    document.getElementById("txt-cantidad-"+id).value = cantidad
    valorPlato = parseInt(document.getElementById("txt-valor-plato-"+id).value)
    document.getElementById("txt-precio-"+id).value = cantidad * valorPlato
}

function minus_comanda(id) {
    cantidad = parseInt(document.getElementById("txt-cantidad-"+id).value)
    if (cantidad > 1) {
        cantidad = cantidad - 1
    }
    document.getElementById("txt-cantidad-"+id).value = cantidad
    valorPlato = parseInt(document.getElementById("txt-valor-plato-"+id).value)
    document.getElementById("txt-precio-"+id).value = cantidad * valorPlato
}