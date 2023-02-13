const links=[
    document.getElementById('home'),
    document.getElementById('users'),
    document.getElementById('agents'),
    document.getElementById('contacts')
]

const url = location.href.toString()

minicrm = url.substring(url.length-8, url.length)

let link

if (minicrm == 'minicrm/') {
    link = 'home'
} else if (url.includes('user')) {
    link = 'users'
} else if (url.includes('contact')) {
    link = 'contacts'
} else if (url.includes('message')) {
    link = 'messages'
} else if (url.includes('landing')) {
    link = 'dashboard'
} else if (url.includes('agent')) {
    link = 'agents'
}

links.forEach((elem) => {
    if (elem.getAttribute('id') === link){
        elem.classList.add('active')
    } else {
        if (elem.classList.contains('active')){
            elem.classList.remove('active')
        }
    }
})