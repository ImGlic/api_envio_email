from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email_utils import send_email

app = FastAPI()

class EmailRequest(BaseModel):
    name: str  # Novo campo para capturar o nome do usuário
    to: EmailStr
    subject: str
    message: str

@app.post("/send-email/")
def send_email_endpoint(email_request: EmailRequest):
    try:
        send_email(
            email_request.to, 
            email_request.subject, 
            email_request.message, 
            email_request.name  # Passamos o nome do remetente
        )
        return {"status": "Email enviado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar email: {str(e)}")
