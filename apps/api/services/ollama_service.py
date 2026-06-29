import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are MyAI.

You are a lifelong AI assistant.

Always answer in the same language as the user.

If the user speaks Uzbek, answer in Uzbek.

Keep answers concise unless the user asks for details.
"""

def generate(prompt: str):

    payload = {
        "model": "qwen3:4b",
        "system": SYSTEM_PROMPT,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 256,
            "num_ctx": 2048
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    data = response.json()

    return data.get("response", "")