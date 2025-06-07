document.addEventListener("DOMContentLoaded", function () {
    const editarModal = document.getElementById('editarModal');
    editarModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;

        document.getElementById('edit-tipo').value = button.getAttribute('data-tipo');
        document.getElementById('edit-mensagem').value = button.getAttribute('data-mensagem');
        document.getElementById('edit-status').value = button.getAttribute('data-status');
        
    });
});

