let botao = document.querySelector(".toggle");
let menu = document.querySelector(".menu");

botao.onclick = (e) => {
    menu.classList.toggle('menu-visivel');
    botao.classList.toggle('mudar');
}

menu.onmouseout = (e) => {
    menu.classList.toggle('menu-visivel'); 
    botao.classList.toggle('mudar');
}

window.onscroll = (e) =>{
    menu.classList.remove('menu-visivel'); 
    botao.classList.remove('mudar');
}