from repositories.memory_repository import (
    save_message,
    get_history
)


def add_user_message(user_id: str, message: str):
    save_message(
        user_id,
        "user",
        message
    )


def add_assistant_message(user_id: str, message: str):
    save_message(
        user_id,
        "assistant",
        message
    )


def load_history(user_id: str):

    rows = get_history(user_id)

    messages = []

    for role, content in rows:

        messages.append({
            "role": role,
            "content": content
        })

    return messages