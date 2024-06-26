var nombre = document.querySelector("#nombre");
var tamaño = document.querySelector("#tamaño");
var precio = document.querySelector("#precio");
var cuenta = document.querySelector("#total"); //Pq ya existe otra llamada total en shoppingcart
var rm = document.querySelector("#rm"); // remove buttons


function shoppingCart() {
    var pedidos = JSON.parse(localStorage.getItem('pedidos'));
    var total = localStorage.getItem('total');
    var carritoSize = pedidos.length;

    nombre.innerHTML = '<h3>Nombre</h3>';
    tamaño.innerHTML = '<h3>Tamaño</h3>';
    precio.innerHTML = '<h3>Precio</h3>';
    rm.innerHTML = '';


    for (let i = 0; i < carritoSize; i++) {
        // Create a container for each item with name and remove button
    var itemContainer = document.createElement('div');
    itemContainer.classList.add('pedido-item');  // Add a class for styling

    var removeButton = document.createElement('button');
    removeButton.classList.add('btn-danger');
    removeButton.textContent = 'X';
    removeButton.onclick = function() { removeItem(i); };  // Set onclick function

    var itemName = document.createElement('h4');
    itemName.textContent = pedidos[i][0];

    // Ensure button and name are aligned vertically
    itemContainer.style.display = 'flex';  // Use flexbox for alignment
    itemContainer.style.alignItems = 'center';  // Center items vertically

    itemContainer.appendChild(removeButton);
    itemContainer.appendChild(itemName);

    rm.appendChild(itemContainer); // Append the container to rm

        nombre.innerHTML += '<h4>' + pedidos[i][0] + '</h4>';
        tamaño.innerHTML += '<h4>' + pedidos[i][1] + '</h4>';
        precio.innerHTML += '<h4>' + pedidos[i][2] + '</h4>';
    }
    cuenta.innerHTML = 'Total: $' + total;
}

shoppingCart();

function removeItem(n){
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

    shoppingCart();
}

//Ajax

var note = document.querySelector('#Comentario');

function pedido(){
    var msg = note.value;
    var mesaNum = document.getElementById('mesa-input').value; // Obtener el número de mesa seleccionado
    var pedidos = localStorage.getItem('pedidos');
    var total = localStorage.getItem('total');

    var ur = "/food/pedido/";
    var pedidoData = {};
    pedidoData['pedidos'] = pedidos;
    pedidoData['note'] = msg;
    pedidoData['cuenta'] = total;
    pedidoData['mesa'] = mesaNum; // Agregar el número de mesa al objeto de datos del pedido

    $.ajax({
        url: ur,
        type: "POST",
        data: pedidoData,
        success: function(data){
            window.location.replace('/food/exito/');
            localStorage.setItem('pedidos', JSON.stringify([]));
            localStorage.setItem('total', 0);
        }
    });
}



