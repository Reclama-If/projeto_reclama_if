document.addEventListener('DOMContentLoaded', function () {
    const deletarModal = document.getElementById('deletarModal'); // Corrigido aqui

    if (deletarModal) {
        deletarModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            if (!button) return;

            const id = button.getAttribute('data-id');
            document.getElementById('delId').value = id;
        });
    }
});
