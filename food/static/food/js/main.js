

var hours = 24; //Para clear data cada 24 hs
var now = new Date().getTime(); // hora de cuando el usr visita la app
var stepTime = localStorage.getItem('stepTime'); // Para saber si usr entro en las ultimas 24hs

if (stepTime == null){ // Si es igual a null es la primera vez que entra
    localStorage.setItem('stepTime', now);

}else{ // Si el usuario ya visito la pagina
    if(now - stepTime > hours*60*60*1000){ // Si visito hace mas de 24 hs
        localStorage.clear(); //borramos lo anterior
        localStorage.setItem('stepTime', now);
    }
}

var pedidos = JSON.parse(localStorage.getItem('pedidos'));
// json.parse convierte js en un array creo
var total = localStorage.getItem('total');

if (pedidos === null || pedidos === undefined){
    localStorage.setItem('pedidos', JSON.stringify([]));
    pedidos = JSON.parse(localStorage.getItem('pedidos'));
}

if (total === null || total === undefined){
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total'); // Cambiar pedidos a total
}


var carrito = document.querySelector("#carrito");
carrito.innerHTML = pedidos.length; //El numero de items
