#Importação do sqlalchemy para as funções ligadas ao BD
from flask_sqlalchemy import SQLAlchemy

#Importa a conexão com banco de dados
from models.conexao import *

from models.tabelas import *

def consultaGeralManifestacoes():
    manifestacoesQuery = Manifestacao.query.all()

    manifestacoesDic = [manifestacao.trans_dic() for manifestacao in manifestacoesQuery]

    return manifestacoesDic

def consultaGeralManifestantes():
    manifestantesQuery = Manifestante.query.all()

    manifestantesDic = [manifestacao.trans_dic() for manifestacao in manifestantesQuery]

    return manifestantesDic
