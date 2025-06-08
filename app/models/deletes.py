#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

from models.tabelas import *

def delManifestacao(manifestacao):
    if(manifestacao):
        db.session.delete(manifestacao)
        db.session.commit()