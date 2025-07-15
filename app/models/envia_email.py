from flask_sqlalchemy import SQLAlchemy
from models.conexao import *
from models.tabelas import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    # Configurações do servidor
    smtp_server = "smtp.gmail.com"  # Corrigido: aspas ao redor do endereço
    smtp_port = 587
    remetente = "reclamaifce@gmail.com"  # Corrigido: nome da variável
    senha = "wojn pkhs mgko qqih"  

    # Criação da mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(mensagem, 'html'))

    try: 
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Usa TLS para segurança
        server.login(remetente, senha)  # Login no servidor SMTP

        # Envia o e-mail
        server.sendmail(remetente, destinatario, msg.as_string())
        print("Email enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar email: {e}")

    finally:
        server.quit()  # Encerra a conexão com o servidor SMTP

# Exemplo de uso

