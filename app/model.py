from main import *
from flask_sqlalchemy import SQLAlchemy
import os

diretorio = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(diretorio, 'database', 'reclamaif.db')

db = SQLAlchemy(app)

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(10), nullable=False)
    autoria = db.Column(db.String(100), nullable=False)

class Manifestante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)

class Manifestacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(500), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    autoria = db.Column(db.String(100), nullable=False)
    anonimato = db.Column(db.Boolean, nullable=False)
    canal_manifestacao = db.Column(db.String(20), nullable=True)


def cadastrarManifestante(nome, email, telefone):
    novo_manifestante = Manifestante(nome=nome, email=email, telefone=telefone)
    db.session.add(novo_manifestante)
    db.session.commit()

def cadastrarManiftt(nome, manifesto, tipo_manifesto, identificacao, anonimato, canal_manifestante, email, telefone,):
    novo_manifestante = Manifestante(nome=nome, email=email, telefone=telefone)
    nova_manifestacao = Manifestacao(mensagem = manifesto, tipo = tipo_manifesto, autoria = identificacao, anonimato = anonimato, canal_manifestacao = canal_manifestante )
    db.session.add(novo_manifestante)
    db.session.add(nova_manifestacao)
    db.session.commit()