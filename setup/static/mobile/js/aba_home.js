document.addEventListener('DOMContentLoaded', function() {
    
    // Verifica se a URL atual contém '/mobile/home'
    const novoAtendimento = document.getElementById('novoAtendimento');

    novoAtendimento.addEventListener('click', function() {
        window.location.href = '/mobile/novo-atendimento/'
    })



});




