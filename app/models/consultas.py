#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

from models.tabelas import *

def consultaGeralManifestacao():
    manifestacoesQuery = Manifestacao.query.all()

    manifestacoesDic = [manifestacao.trans_dic() for manifestacao in manifestacoesQuery]

    return manifestacoesDic