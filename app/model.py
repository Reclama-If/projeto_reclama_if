#Importa as definições das tabelas do BD
from models.tabelas import *

#Importa os cadastros das tabelas do BD
from models.cadastros import *

def consultaGeralManifestacao():
    manifestacoesQuery = Manifestacao.query.all()

    manifestacoesDic = [manifestacao.trans_dic() for manifestacao in manifestacoesQuery]

    return manifestacoesDic