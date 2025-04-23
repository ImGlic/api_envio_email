import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email: str, subject: str, message: str, sender_name: str, email_from: str None):
    email = EmailMessage()
    email["From"] = os.getenv("EMAIL_USER")
    email["To"] = to_email
    email["Subject"] = subject
    # email["Reply-To"] = reply_to

    email.set_content(message)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #0a0a23;
                font-family: 'Segoe UI', sans-serif;
            }}
            .container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }}
            h1 {{
                color: #6C63FF;
                font-size: 24px;
                margin-bottom: 20px;
            }}
            p {{
                color: #333;
                font-size: 16px;
                line-height: 1.6;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                text-align: center;
                color: #aaa;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📩 Novo contato via portfólio</h1>
            <p><strong>Nome:</strong> {sender_name}</p>  <!-- Nome do remetente -->
            <p><strong>Assunto:</strong> {subject}</p>
            <p><strong>Mensagem:</strong></p>
            <p>{message}</p>
            <div class="footer">
                Esta mensagem foi enviada pelo seu formulário do portfólio.
            </div>
        </div>
    </body>
    </html>
    """

    email.add_alternative(html_content, subtype="html")

    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(email)
