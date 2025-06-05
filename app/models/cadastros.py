#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

def cadastrarManifestante(nome, email, telefone):
    novo_manifestante = Manifestante(nome=nome, email=email, telefone=telefone)
    db.session.add(novo_manifestante)
    db.session.commit()


def cadastrarManiftt(nome, email, telefone, mensagem, tipo, autoria, anonimato, canal_manifestacao):
    novo_manifestante = Manifestante(nome = nome, email = email, telefone = telefone)
    nova_manifestacao = Manifestacao(mensagem = mensagem, tipo = tipo, status = "P", autoria = autoria, anonimato = anonimato, canal_manifestacao = canal_manifestacao )
    db.session.add(novo_manifestante)
    db.session.add(nova_manifestacao)
    db.session.commit()