from flask_sqlalchemy import SQLAlchemy
from models.conexao import *
from models.tabelas import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(email, nome, assunto, mensagem):
    # Configurações do servidor
    smtp_server = "smtp.gmail.com"  # Corrigido: aspas ao redor do endereço
    smtp_port = 587
    remetente = "reclamaifce@gmail.com"  # Corrigido: nome da variável
    senha = "wojn pkhs mgko qqih"  

    print("Email asenviado com sucesso!")
    # Criação da mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = email
    msg["Subject"] = assunto

    mensagem_html = f"""
    <!DOCTYPE html>
    <html lang='pt-br'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Ouvidoria - IFCE CRATO</title>
        <style>
        * {{
            margin: 0 auto;
            padding: 0 auto;
        }}

        @media(max-width: 1120px) {{
            body {{
                background-image: linear-gradient(to bottom, #FFFFFF 30% , #FFFFFF 10%) !important;
            }}
            .topo {{
                width: 100% !important;
                padding: 10px 0px !important;
                background-color: #086e01 !important;
            }}
            .container {{
                width: 100% !important;
                margin-top: 0px !important;
                border-radius: 0px !important;
            }}
            .header {{
                padding: 6px 0px !important;
            }}
            .titulo {{
                font-size: 22px !important;
            }}
            .informacao_pessoa {{
                width: 87% !important;
            }}
            .nome {{
                font-size: 16px !important;
            }}
            .email {{
                font-size: 16px !important;
            }}
            .texto {{
                font-size: 15px !important;
            }}
            .logo {{
                margin-top: 15px !important;
                width: 280px !important;
                height: 65px !important;
            }}
            .footer {{
                border-radius: 0px !important;
                width: 100% !important;
                padding: 20px 0px !important;
            }}
            .footer span {{
                font-size: 16px !important;
            }}
        }}
        </style>
    </head>

    <body style='display: inline-block;
        background-image: linear-gradient(to bottom, #086e01 30% , #f0f3f7 10%);
        width: 100%;
        text-align: center;
        font-family: poppins, sans-serif;
        background-repeat: no-repeat;'>

        <div class='fundo' style='width: 100%; padding-bottom: 70px;'>
            <div class='topo'></div>
            <div class='container' style='margin-top: 80px;
                background-color: white;
                width: 55%;
                padding: 10px 0;
                text-align: center;
                box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.3);
                border-radius: 15px 15px 0px 0px;'>

                <div class='header' style='width: 87%;
                    padding: 12px 0px;
                    margin-top: 6px;
                    margin-bottom: 5px;
                    text-align: center;'>
                    <h1 class='titulo' style='color: #1C1C1C;
                        font-size: 30px;
                        letter-spacing: 1px;'>Ouvidoria - Reclama IF</h1>
                </div>

                <hr style='border-color: #013B95; border-top: 1px; margin-bottom: 13px; width: 87%;'>

                <div class='main' style='text-align: left;
                    display: inline-block;
                    width: 100%;'>

                    <div class='informacao_pessoa' style='width: 87%;
                        display: flex;
                        margin-bottom: 27px;'>
                        <span class='nome' style='width: 50%;
                            padding-right: 10px;
                            text-align: right;
                            font-size: 18px;
                            font-weight: 400;'>{nome}</span>
                        <hr style='border-color: #013B95; border-top: 1px;'>
                        <span class='email' style='width: 50%;
                            padding-left: 10px;
                            text-align: left;
                            font-size: 18px;
                            font-weight: 400;
                            font-style: italic;
                            color: #013B95;'>{email}</span>
                    </div>

                    <p class='texto' style='width: 87%;
                        margin-top: 0px;
                        margin-bottom: 15px;
                        font-size: 17px;
                        font-weight: 400;
                        text-align: justify;'>
                        {mensagem}
                    </p>
               

                    <div id='logo' style='width: 100%; text-align: center;'>
                        <img src='https://ifce.edu.br/prpi/documentos-1/semic/2019/logos_ifce_horizontal/@@images/image.png' alt='Logo Unileão' class='logo' style='width: 340px;
                            height: 90px;
                            margin-bottom: 20px;'>
                    </div>
                </div>
            </div>

            <div class='footer' style='text-align: center;
                width: 55%;
                background-color: #086e01;
                padding: 12px 0px;
                border-radius: 0px 0px 15px 15px;
                box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.3);'>
                <span style='color: #ffffff;
                    font-size: 17px;'>Instituto Federal de Educação, Ciência e Tecnologia do Ceará&copy; </span>
            </div>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(mensagem_html, 'html'))

    try: 
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Usa TLS para segurança
        server.login(remetente, senha)  # Login no servidor SMTP

        # Envia o e-mail
        server.sendmail(remetente, email, msg.as_string())
     

    except Exception as e:
        print(f"Erro ao enviar email: {e}")

    finally:
        server.quit()  # Encerra a conexão com o servidor SMTP

# Exemplo de uso

