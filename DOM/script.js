const h1 = document.getElementById('titulo')
let texto = h1.innerHTML;
const teste = document.querySelector('#titulo'); //id
teste.innerHTML = 'outro-titulo' // alterando a propriedade 

// acessando e alterando estilos 
const p = document.querySelector('#estilo')
p.style.textTransform = 'uppercase';

//Alterando elementos internos
const ul = document.querySelector('#lista')
const item = document.createElement('li')
item.textContent = 'Espirito Santo'
ul.appendChild(item);
item.remove();


//escutando evento
const a = document.querySelector('a')

a.addEventListener('click', function(event){
event.preventDefault() //faz com que o clique não aconteça
window.alert("Fui clicado")
})