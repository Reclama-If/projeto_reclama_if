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

#Rota para cadastrar manifestação e manifestante

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
    manifestantes = consultaGeralManifestantes()

    if(verificaExisteManifestante(email, manifestantes)[0]):
        id_manifestante = verificaExisteManifestante(email, manifestantes)[1]

        cadastrarManiftc(manifesto, tipoManifesto, identificacao, anonimato, canal_manifestante, id_manifestante)
    else:
        cadastrarManiftt(nome, email, telefone)

        id_manifestante = verificaExisteManifestante(email, manifestantes)[1]

        cadastrarManiftc(manifesto, tipoManifesto, identificacao, anonimato, canal_manifestante, id_manifestante)

    return redirect('/consultar_manifesto')

@app.route('/consultar_manifesto')
def consultarManifc():
    manifestacoes = consultaGeralManifestacoes()
    manifestantes = consultaGeralManifestantes()

    return render_template('home.html', manifestacoes=manifestacoes, manifestantes=manifestantes)

@app.route('/editar_manifesto', methods=['POST'])
def editarManifestacaoEmanifestante():
    id_manifestante = request.form.get('editIdManifestante')
    nome = request.form.get('editNome')
    email = request.form.get('editEmail')
    telefone = request.form.get('editTelefone')

    id = request.form.get('editId')
    mensagem = request.form.get('editManifesto')
    tipo = request.form.get('editTipo')
    autoria = request.form.get('editIdentificacao')

    anonimato = 'Sim' if request.form.get('editAnonimato') == 'on' else 'Não'

    canal_manifestacao = request.form.get('edit_canal_da_manifestacao')
    
    manifestacao = consultaEspManifestacao(id)[0]
    manifestante = consultaEspManifestante(id_manifestante)[0]

    editManifestacao(manifestacao, mensagem, tipo, autoria, anonimato, canal_manifestacao)
    editManifestante(manifestante, nome, email, telefone)

    return redirect('/consultar_manifesto')

@app.route('/deletar_manifesto', methods=['POST'])
def delManiftc():
    id = request.form.get('delId')
    
    manifestacao = consultaEspManifestacao(id)[0]

    delManifestacao(manifestacao)

    return redirect('/consultar_manifesto')