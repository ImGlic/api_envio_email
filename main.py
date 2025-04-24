from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email_utils import send_email
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://portifolioatual-xi.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    name: str 
    to: EmailStr
    subject: str
    message: str,
    email_from: EmailStr

@app.post("/send-email/")
def send_email_endpoint(email_request: EmailRequest):
    try:
        send_email(
            to_email=email_request.to, 
            subject=email_request.subject, 
            message=email_request.message, 
            sender_name=email_request.name,
            reply_to=email_request.email_from
        )
        return {"status": "Email enviado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar email: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
