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

def consultaEspManifestacao(id):
    manifestacaoQuery = Manifestacao.query.get(id)

    if(manifestacaoQuery):
        manifestacaoDic = manifestacaoQuery.trans_dic()

        return manifestacaoQuery, manifestacaoDic

def consultaEspManifestante(id):
    manifestanteQuery = Manifestante.query.get(id)

    if(manifestanteQuery):
        manifestanteDic = manifestanteQuery.trans_dic()

        return manifestanteQuery, manifestanteDic