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


@app.route('/cadastrar_manifesto', methods=['POST'])
def cadastrarManifesto():
    nome = request.form['usuario']
    email = request.form['email']
    telefone = request.form['telefone']
    manifesto = request.form['manifesto']
    tipoManifesto = request.form['tipoManifesto']
    identificacao = request.form['identificacao']

    if(request.form['anonimato'] != None):
        anonimato = request.form['anonimato']
    else:
        anonimato = "Não"

    canal_manifestante = "Sis.ouvidoria"

    cadastrarManiftt(nome, email, telefone, manifesto, tipoManifesto, identificacao, anonimato, canal_manifestante)

    return redirect('/consultar_manifesto')

@app.route('/consultar_manifesto')
def consultarManifc():
    manifestacoes = consultaGeralManifestacao()

    return render_template('home.html', manifestacoes=manifestacoes)

