#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

from models.tabelas import *

def editManifestacao(manifestacao, mensagem, tipo, autoria, anonimato, canal_manifestacao):
    if(manifestacao):
        manifestacao.mensagem = mensagem
        manifestacao.tipo = tipo
        manifestacao.autoria = autoria
        manifestacao.anonimato = anonimato
        manifestacao.canal_manifestacao = canal_manifestacao

        db.session.commit()

def editManifestante(manifestante, nome, email, telefone):
    if(manifestante):
        manifestante.nome = nome
        manifestante.email = email
        manifestante.telefone = telefone

        db.session.commit