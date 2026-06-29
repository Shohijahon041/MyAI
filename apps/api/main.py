from fastapi import FastAPI

app = FastAPI(
    title="MyAI",
    version="0.4.0"
)

@app.get("/")
def root():
    return {
        "name": "MyAI",
        "version": "0.4.0",
        "status": "running",
        "message": "Welcome to MyAI"
    }