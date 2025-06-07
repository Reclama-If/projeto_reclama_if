#importação do flask
from flask import Flask

#Inicialização do flask
app = Flask(__name__)

#imporação das rotas
from routes import *

#Ativação do debug caso o main esteja rodando
if __name__ == '__main__':
    app.run(debug=True)
