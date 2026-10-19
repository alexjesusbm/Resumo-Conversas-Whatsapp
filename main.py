from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"message": "Aplicação Funcionando"}

@app.post("/mensagens")
def receber_mensagem():
    return {"message": "mensagem recebida"} 

