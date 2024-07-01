var nombre = document.querySelector("#nombre");
var tamaño = document.querySelector("#tamaño");
var precio = document.querySelector("#precio");
var cuenta = document.querySelector("#total");
var rm = document.querySelector("#rm");

function shoppingCart() {
    var pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];
    var total = localStorage.getItem('total') || 0;
    var carritoSize = pedidos.length;

    nombre.innerHTML = '<h3>Nombre</h3>';
    tamaño.innerHTML = '<h3>Tamaño</h3>';
    precio.innerHTML = '<h3>Precio</h3>';
    rm.innerHTML = '';

    for (let i = 0; i < carritoSize; i++) {
        var itemContainer = document.createElement('div');
        itemContainer.classList.add('pedido-item');
        
        var removeButton = document.createElement('button');
        removeButton.classList.add('btn', 'btn-danger2');
        removeButton.textContent = 'X';
        removeButton.onclick = function() { removeItem(i); };

        itemContainer.appendChild(removeButton);
        rm.appendChild(itemContainer);

        nombre.innerHTML += '<h4>' + pedidos[i][0] + '</h4>';
        tamaño.innerHTML += '<h4>' + pedidos[i][1] + '</h4>';
        precio.innerHTML += '<h4>' + pedidos[i][2] + '</h4>';
    }
    cuenta.innerHTML = 'Total: $' + total;
}

shoppingCart();

function removeItem(n) {
    var pedidos = JSON.parse(localStorage.getItem('pedidos')) || [];
    var total = localStorage.getItem('total') || 0;

    pedidos[n][2] = pedidos[n][2].replace(',', '.');
    total = Number(total) - Number(pedidos[n][2]);
    pedidos.splice(n, 1);

    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length;

    localStorage.setItem('pedidos', JSON.stringify(pedidos));
    localStorage.setItem('total', total);

    shoppingCart();
}

var note = document.querySelector('#Comentario');

function pedido() {
    var msg = note.value;
    var mesaNum = document.getElementById('mesa-input').value;
    var total = parseFloat(localStorage.getItem('total')) || 0;

    var errorContainer = document.querySelector('.error-container');
    errorContainer.style.display = 'none';  // Ocultar cualquier alerta previa
    
    if (!mesaNum) {
        errorContainer.innerHTML = 'Por favor seleccione una mesa.';
        errorContainer.style.display = 'block';
        return;
    }

    if (total === 0) {
        errorContainer.innerHTML = 'No se puede realizar un pedido con un total de 0.00.';
        errorContainer.style.display = 'block';
        return;
    }

    var pedidos = localStorage.getItem('pedidos');

    var ur = "/food/pedido/";
    var pedidoData = {
        'pedidos': pedidos,
        'note': msg,
        'cuenta': total,
        'mesa': mesaNum
    };

    $.ajax({
        url: ur,
        type: "POST",
        data: pedidoData,
        success: function(data) {
            window.location.replace('/food/exito/');
            localStorage.setItem('pedidos', JSON.stringify([]));
            localStorage.setItem('total', 0);
        }
    });
}
