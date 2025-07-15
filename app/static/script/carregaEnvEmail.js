document.addEventListener('DOMContentLoaded', function () {
    const editarModal = document.getElementById('responderModal');

    if (editarModal) {
        editarModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;

            if (!button) return;

            const id = button.getAttribute('data-id');
            const id_manifestante = button.getAttribute('data-id-manifestante');
            const email = button.getAttribute('data-email');

            document.getElementById('resEmail').value = email;

        });
    }
});
