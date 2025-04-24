import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email: str, subject: str, message: str, sender_name: str, reply_to: str):
    email = EmailMessage()
    email["From"] = os.getenv("EMAIL_USER")
    email["To"] = to_email
    email["Subject"] = subject
    email["Reply-To"] = reply_to

    email.set_content(message)

   html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 40px 20px;
                background-color: #111827;
                font-family: 'Segoe UI', sans-serif;
                color: #111827;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background-color: #ffffff;
                border-radius: 12px;
                padding: 30px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
            }}
            .header {{
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 24px;
            }}
            .header h1 {{
                font-size: 22px;
                color: #6C63FF;
                margin: 0;
            }}
            .label {{
                font-weight: 600;
                margin-bottom: 4px;
                color: #111827;
            }}
            .value {{
                margin: 0 0 16px 0;
                color: #374151;
            }}
            .message-box {{
                background-color: #f9fafb;
                padding: 16px;
                border-radius: 8px;
                white-space: pre-wrap;
                color: #374151;
            }}
            .footer {{
                margin-top: 32px;
                font-size: 12px;
                color: #9ca3af;
                text-align: center;
            }}
            a {{
                color: #6C63FF;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://img.icons8.com/fluency/48/secured-letter.png" width="32" />
                <h1>Novo contato via portfólio</h1>
            </div>

            <p class="label">Nome:</p>
            <p class="value">{sender_name}</p>

            <p class="label">Assunto:</p>
            <p class="value">{subject}</p>

            <p class="label">Mensagem:</p>
            <div class="message-box">
                <p>Email do usuário: <a href="mailto:{email_from}">{email_from}</a></p>
                <p>{message}</p>
            </div>

            <div class="footer">
                Esta mensagem foi enviada a partir do seu formulário no portfólio.
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
