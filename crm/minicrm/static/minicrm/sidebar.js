const hamb = document.querySelector('.hamburger')


hamb.addEventListener('click', ()=>{
    const menu = document.querySelector('.menu')
    menu.classList.toggle('menu-active')

    hamb.classList.toggle('checked')
})