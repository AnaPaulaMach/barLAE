// en lugar de p tenia que ser h de hamburguesa 
var pcarrito = document.querySelector('#pcarrito');
var ptotal = document.querySelector('#ptotal');

// add Hamburguesa
function addHamburguesa(hid) { // hamburgues id = hid
    // get hamburguesa name
    var hamburguesaId = '#ham' + hid; // no confundir id html e id de la BD
    var nombre = document.querySelector(hamburguesaId).innerHTML;
    // get hamburguesa price
    var radio = '[name="hamburguesa' + hid + '"]';
    var pre = document.querySelectorAll(radio);
    var size, precio;
    if (pre[0].checked) {
        precio = pre[0].value;
        size = '1'; // Una Hamburguesa/Carne
    } else {
        precio = pre[1].value;
        size = '2'; // Dos Hamburguesa/Carne
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

    total = Number(total) + Number(precio);
    localStorage.setItem('total', total);

    //Updating number of items in shopping Cart
    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length; //El numero de items

    butto = '<div class="del" onclick="removeHamburguesa(' + carritoSize +')"></div>';
    ptotal.innerHTML = 'Total: $' + total;
    pcarrito.innerHTML += '<li class="cart-item">' + nombre + ' ' + size + ': $' + precio + butto +'</li>';
}

function pshoppingCart() {
    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    var total = localStorage.getItem('total');
    var carritoSize = pedidos.length;
    pcarrito.innerHTML = '';
    for (let i = 0; i < carritoSize; i++) {
        let butto = '<div class="del" onclick="removeHamburguesa(' + i + ')"></div>';
        pcarrito.innerHTML += '<li class="cart-item">' + pedidos[i][0] + ' ' + pedidos[i][1] + ': $' + pedidos[i][2] + butto + '</li>';
    }
    ptotal.innerHTML = 'Total: $' + total;
}

pshoppingCart();


// Eliminar Hamburguesa, argumento numero el indice de la hambu
function removeHamburguesa(n){
    //get para obtener valores
    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    var total = localStorage.getItem('total');

    total = Number(total) - Number(pedidos[n][2]);
    pedidos.splice(n,1); // 1 el numero de items que queremos remover

    //Updating number of items in shopping Cart
    var carrito = document.querySelector("#carrito");
    carrito.innerHTML = pedidos.length; //El numero de items
    
    //set para guardar valores
    localStorage.setItem('pedidos', JSON.stringify(pedidos));
    localStorage.setItem('total', total);

    pshoppingCart();
}