#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

#Importa o "UserMixin" para configurar as tabelas rnvolvidas no sistema de login
from flask_login import UserMixin

class Administrador(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(10), nullable=False)
    autoria = db.Column(db.String(100), nullable=False)

    def trans_dic(self):
        return {coluna.name: getattr(self, coluna.name) for coluna in self.__table__.columns}


class Manifestante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)

    def trans_dic(self):
        return {coluna.name: getattr(self, coluna.name) for coluna in self.__table__.columns}

class Manifestacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(500), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    autoria = db.Column(db.String(100), nullable=False)
    anonimato = db.Column(db.String(10), nullable=False)
    canal_manifestacao = db.Column(db.String(20), nullable=True)
    id_manifestante = db.Column(db.Integer, nullable=False)

    def trans_dic(self):
        return {coluna.name: getattr(self, coluna.name) for coluna in self.__table__.columns}
