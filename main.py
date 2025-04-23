from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email_utils import send_email
import os
import uvicorn

app = FastAPI()

class EmailRequest(BaseModel):
    name: str 
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
            email_request.name
        )
        return {"status": "Email enviado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar email: {str(e)}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)