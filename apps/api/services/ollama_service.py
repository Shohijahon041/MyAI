import requests

from services.memory.memory_service import (
    add_user_message,
    add_assistant_message,
    load_history
)

OLLAMA_URL = "http://localhost:11434/api/chat"

SYSTEM_PROMPT = """
You are MyAI.

You are a lifelong AI assistant.

Always answer in the same language as the user.

If the user writes in Uzbek, answer in Uzbek.

Be concise unless the user asks for detail.
"""


def generate(user_id: str, prompt: str):

    add_user_message(user_id, prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(load_history(user_id))

    payload = {
        "model": "qwen3:4b",
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_ctx": 4096
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    data = response.json()

    answer = data["message"]["content"]

    add_assistant_message(user_id, answer)

    return answer