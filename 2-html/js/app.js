
var ans = document.getElementById('answer');
var qns = prompt('Cuál es su Nombre ?');

if(qns === 'Ofac') {
	ans.innerHTML = "Bienvenido Administrador: "+qns;
} else {
	ans.innerHTML = "Bienvenido Visitante: "+qns;
}