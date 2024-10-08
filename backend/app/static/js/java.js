
// Modal Hardware - Botão de hardware
document.getElementById('botão-hardware').addEventListener('click', function () {
    document.querySelector('.bg-modal').style.display = 'flex';
    document.querySelector('.modal-content-hardware').style.display = 'block'
});


// Modal Descrição - Botão de software
document.getElementById('botão-software').addEventListener('click', function () {
    document.querySelector('.bg-modal').style.display = 'flex';
    // vai ser descrição temporáriamente, depois vai virar prob. de software
    document.querySelector('.modal-content-descrição').style.display = 'block'
});

// Modal Descrição - Botão de Login
document.getElementById('botão-login').addEventListener('click', function () {
    document.querySelector('.bg-modal').style.display = 'flex';
    // vai ser descrição temporáriamente, depois vai virar prob. de software
    document.querySelector('.modal-content-login').style.display = 'block'
});

function abrir() {
    document.querySelector('.bg-modal').style.display = 'flex';
}

// Mudar para Modal descrição
function descrição() {
    document.querySelector('.modal-content-hardware').style.display = 'none'
    document.querySelector('.modal-content-descrição').style.display = 'block'
    document.querySelector('.modal-content-login').style.display = 'none'
}



// Fechar modais
function fechar() {
    document.querySelector('.bg-modal').style.display = 'none';
    document.querySelector('.modal-content-hardware').style.display = 'none'
    document.querySelector('.modal-content-descrição').style.display = 'none'
    document.querySelector('.modal-content-login').style.display = 'none'
}

