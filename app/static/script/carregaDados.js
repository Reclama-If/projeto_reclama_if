document.addEventListener('DOMContentLoaded', function () {
    const editarModal = document.getElementById('editarModal');

    if (editarModal) {
        editarModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;

            if (!button) return;

            const id = button.getAttribute('data-id');
            const tipo = button.getAttribute('data-tipo');
            const mensagem = button.getAttribute('data-mensagem');
            const status = button.getAttribute('data-status');
            const autoria = button.getAttribute('data-autoria');
            const anonimato = button.getAttribute('data-anonimato');
            const canal = button.getAttribute('data-canal');
            const id_manifestante = button.getAttribute('data-id-manifestante');
            const nome = button.getAttribute('data-nome');
            const email = button.getAttribute('data-email');
            const telefone = button.getAttribute('data-telefone');

            document.getElementById('editId').value = id;
            document.getElementById('editTipo').value = tipo;
            document.getElementById('editManifesto').value = mensagem;
            document.getElementById('editIdentificacao').value = autoria;
            document.getElementById('edit_canal_da_manifestacao').value = canal;

            document.getElementById('editIdManifestante').value = id_manifestante;
            document.getElementById('editNome').value = nome;
            document.getElementById('editEmail').value = email;
            document.getElementById('editTelefone').value = telefone;

            document.getElementById('editAnonimato').checked = (anonimato === "Sim");

            console.log("Modal de edição aberto com sucesso.");
        });
    }
});
