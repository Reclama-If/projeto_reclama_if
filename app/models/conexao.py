#Importa o "main" para puxar o objeto "app"
from main import *

#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa o os para a ultilização segura de caminhos de arquivos (usando caminhos relativos dinâmicos)
import os

#Importa a conexão com banco de dados
from models.conexao import *

diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(diretorio, 'database', 'reclamaif.db')

db = SQLAlchemy(app)