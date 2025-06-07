#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

from models.tabelas import *

def cadastrarManiftt(nome, email, telefone):
    novo_manifestante = Manifestante(nome=nome, email=email, telefone=telefone)
    db.session.add(novo_manifestante)
    db.session.commit()


def cadastrarManiftc(mensagem, tipo, autoria, anonimato, canal_manifestacao, id_manifestante):
    nova_manifestacao = Manifestacao(mensagem = mensagem, tipo = tipo, status = "P", autoria = autoria, anonimato = anonimato, canal_manifestacao = canal_manifestacao, id_manifestante = id_manifestante)
    db.session.add(nova_manifestacao)
    db.session.commit()