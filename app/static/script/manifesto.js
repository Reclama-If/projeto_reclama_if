function envia_Manifesto() {
    // Pegando os valores dos campos do html e atribuindo a variáveis do javascript
    let usuario = document.getElementById('usuario').value
    let email = document.getElementById('email').value
    let telefone = document.getElementById('telefone').value
    let tipo = document.getElementById('tipoManifesto').value
    let identificacao = document.getElementById('identificacao').value
    let manifesto = document.getElementById('manifesto').value
    let formulario = document.getElementById("form_manifesto")
    let checkboxAnonimato = document.getElementById("anonimato")
    let anonimato = null


    if (checkboxAnonimato.checked) {
        anonimato = 1
    } else {
        anonimato = 0
    }

    let regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/

    if (usuario == '' || email == '' || telefone == '' || tipo == '' || identificacao == '' || manifesto == '') {

        // Fazer tratamento de erros aqui e retorno pro usuario
 
    } else {
         const dados = {
            Nome: usuario,
            Email: email,
            Telefone: telefone,
            Mensagem: manifesto,
            Tipo_da_mensagem: tipo,
            Identificação: identificacao
          
        }
        
        // enviando pro py
               
        fetch('/dados_manifestacao', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(dados)
        })
        .then(response => response.json())
        .then(data => console.log(data));


            
        
    }
}