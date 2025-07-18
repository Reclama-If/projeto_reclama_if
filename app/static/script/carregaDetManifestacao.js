document.addEventListener('DOMContentLoaded', function () {
    const detModal = document.getElementById('detModal');

    if (detModal) {
        detModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;

            if (!button) return;

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
           

            document.getElementById('detStatus').innerHTML = status;
            document.getElementById('detTipo').innerHTML = tipo;
            document.getElementById('detManifesto').innerHTML = mensagem;
            document.getElementById('detReferenciamentoManifestante').innerHTML = autoria;
            document.getElementById('detCanalManifestacao').innerHTML = canal;
            document.getElementById('detNomeManifestante').innerHTML = nome;
            document.getElementById('detEmailManifestante').innerHTML = email;
            document.getElementById('detTelefoneManifestante').innerHTML = telefone;


        

            document.getElementById('editAnonimato').checked = (anonimato === "Sim");
        });
    }
});

