#Importações do Flask
from main import *
from model import *
from flask import render_template, request, redirect

#Importações de arquivos.py


#Rotas
#Rota para página principal
@app.route('/')
def homepage():
    return render_template('manifesto.html')

#Rota para página para cadastrar manifestante
@app.route('/cadastrarManifestante')
def telaCadMtt():
    return render_template('cadManifestante.html')

#Rota para cadastrar manifestante
@app.route('/cadastrar', methods=['POST'])
def cadastrarMtt():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    cadastrarManifestante(nome, email, telefone)

    return redirect('/cadastrarManifestante')