
var bcarrito = document.querySelector('#bcarrito');
var btotal = document.querySelector('#btotal');

// add Hamburguesa
function addBebida(bid) { // hamburgues id = hid
    // get hamburguesa name
    var bebidaId = '#beb' + bid; // no confundir id html e id de la BD
    var nombre = document.querySelector(bebidaId).innerHTML;
    // get hamburguesa price
    var radio = '[name="bebida' + bid + '"]';
    var pre = document.querySelectorAll(radio);
    var size, precio;
    if (pre[0].checked) {
        precio = pre[0].value;
        size = 'C'; // Una Hamburguesa/Carne
    } else {
        precio = pre[1].value;
        size = 'G'; // Dos Hamburguesa/Carne
    }

    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    if (!pedidos) { // Verificar si pedidos es null o undefined
        pedidos = []; // Inicializar pedidos como un array vacío si es null
    }
    var total = localStorage.getItem('total');

    // Saving item and total in localstorage
    var carritoSize = pedidos.length;
    pedidos[carritoSize] = [nombre, size, precio];
    localStorage.setItem('pedidos', JSON.stringify(pedidos));

    precio = precio.replace(',', '.');
    total = Number(total) + Number(precio);
    localStorage.setItem('total', total);

    //Updating number of items in shopping Cart
    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length; //El numero de items

    butto = '<div class="del" onclick="removeBebida(' + carritoSize +')"></div>';
    btotal.innerHTML = 'Total: $' + total;
    bcarrito.innerHTML += '<li class="cart-item">' + nombre + ' ' + size + ': $' + precio + butto +'</li>';
}

function bshoppingCart() {
    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    var total = localStorage.getItem('total');
    var carritoSize = pedidos.length;
    bcarrito.innerHTML = '';
    for (let i = 0; i < carritoSize; i++) {
        let butto = '<div class="del" onclick="removeBebida(' + i + ')"></div>';
        bcarrito.innerHTML += '<li class="cart-item">' + pedidos[i][0] + ' ' + pedidos[i][1] + ': $' + pedidos[i][2] + butto + '</li>';
    }
    btotal.innerHTML = 'Total: $' + total;
}


bshoppingCart();

// Eliminar Bebida, argumento numero el indice de la bebida
function removeBebida(n){
    //get para obtener valores
    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    var total = localStorage.getItem('total');

    pedidos[n][2] = pedidos[n][2].replace(',', '.');
    total = Number(total) - Number(pedidos[n][2]);
    pedidos.splice(n,1); // 1 el numero de items que queremos remover

    //Updating number of items in shopping Cart
    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length; //El numero de items

    //set para guardar valores
    localStorage.setItem('pedidos', JSON.stringify(pedidos));
    localStorage.setItem('total', total);

    bshoppingCart();
}