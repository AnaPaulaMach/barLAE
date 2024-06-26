var bcarrito = document.querySelector('#bcarrito');
var btotal = document.querySelector('#btotal');

// Añadir bebida al carrito
function addBebida(bid) {
    var bebidaId = '#beb' + bid;
    var nombre = document.querySelector(bebidaId).innerHTML;
    var radio = '[name="bebida' + bid + '"]';
    var pre = document.querySelectorAll(radio);
    var size, precio;

    if (pre[0].checked) {
        precio = pre[0].value;
        size = 'C';
    } else {
        precio = pre[1].value;
        size = 'G';
    }

    var pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];
    var total = localStorage.getItem('total') || 0;

    // Guardar el ítem y el total en localStorage
    var carritoSize = pedidos.length;
    pedidos[carritoSize] = [nombre, size, precio];
    localStorage.setItem('pedidos', JSON.stringify(pedidos));

    precio = precio.replace(',', '.');
    total = Number(total) + Number(precio);
    localStorage.setItem('total', total);

    // Actualizar número de ítems en el carrito
    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length;

    var butto = '<div class="del" onclick="removeBebida(' + carritoSize + ')"></div>';
    btotal.innerHTML = 'Total: $' + total;
    bcarrito.innerHTML += '<li class="cart-item">' + nombre + ' ' + size + ': $' + precio + butto + '</li>';
}

function bshoppingCart() {
    var pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];
    var total = localStorage.getItem('total') || 0;
    var carritoSize = pedidos.length;
    bcarrito.innerHTML = '';
    for (let i = 0; i < carritoSize; i++) {
        let butto = '<div class="del" onclick="removeBebida(' + i + ')"></div>';
        bcarrito.innerHTML += '<li class="cart-item">' + pedidos[i][0] + ' ' + pedidos[i][1] + ': $' + pedidos[i][2] + butto + '</li>';
    }
    btotal.innerHTML = 'Total: $' + total;
}

bshoppingCart();

// Eliminar bebida del carrito
function removeBebida(n) {
    var pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];
    var total = localStorage.getItem('total') || 0;

    pedidos[n][2] = pedidos[n][2].replace(',', '.');
    total = Number(total) - Number(pedidos[n][2]);
    pedidos.splice(n, 1);

    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length;

    localStorage.setItem('pedidos', JSON.stringify(pedidos));
    localStorage.setItem('total', total);

    bshoppingCart();
}
