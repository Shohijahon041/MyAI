import requests

from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://127.0.0.1:8000/chat"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 Salom!\nMen MyAI.\nSavolingizni yozing."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text

    payload = {
        "user_id": str(update.effective_user.id),
        "message": user_message
    }

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        answer = data.get("reply", "")

        if not answer:
            answer = "⚠️ MyAI javob qaytarmadi."

    except Exception as e:

        answer = f"❌ Xatolik:\n{e}"

    await update.message.reply_text(answer)