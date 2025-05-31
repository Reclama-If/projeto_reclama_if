from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('/Users/Matheus/Documents/GitHub/projeto_reclama_if/app/view/teste.html')

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    dados = request.json
    print(f"Nome: {dados['nome']}, Email: {dados['email']}, Senha: {dados['senha']}")  # Teste no terminal
    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
