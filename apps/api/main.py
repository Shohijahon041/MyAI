from fastapi import FastAPI
from pydantic import BaseModel

from apps.api.services.ollama_service import generate

app = FastAPI(
    title="MyAI",
    version="0.4.1"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "name": "MyAI",
        "version": "0.4.1",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = generate(request.message)

    return {
        "reply": answer
    }