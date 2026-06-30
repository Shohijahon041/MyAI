from fastapi import FastAPI
from pydantic import BaseModel

from apps.api.services.ollama_service import generate

app = FastAPI(
    title="MyAI",
    version="0.5.2"
)


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.get("/")
def root():
    return {
        "name": "MyAI",
        "status": "running",
        "version": "0.5.2"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer = generate(
        request.user_id,
        request.message
    )

    return {
        "reply": answer
    }