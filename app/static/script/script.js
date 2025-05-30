function enviarDados() {
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;

    let dados = {
        nome: nome,
        email: email,
        senha: senha
    };

    fetch('/receber_dados', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
