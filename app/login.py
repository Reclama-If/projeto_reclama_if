from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

#Importa o "main" para puxar o objeto "app"
from main import *

#Importa uma biblioteca para gerar um token para ser a chave secreta
import secrets

#Configura uma chave secreta para servir de verificação para cokiees de sessão do usuário
if(not(app.config['SECRET_KEY'])):
    app.config['SECRET_KEY'] = secrets.token_hex(32)

#Implementa o gerenciador de logins do "flask login"
login_manager = LoginManager()
login_manager.init_app(app)

#Define para onde o usuario que não estiver logado é redirecionado ao tentar acessar uma rora com "@login_required"
login_manager.login_view = 'login'

#Puxa os dados do usuário logado no momento
@login_manager.user_loader
def load_administrador(user_id):
    return Administrador.query.get(int(user_id))