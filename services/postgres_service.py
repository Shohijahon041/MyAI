from core.database import SessionLocal
from models.memory import Memory


def save_message(user_id: int, role: str, message: str):

    db = SessionLocal()

    try:
        db.add(
            Memory(
                user_id=user_id,
                role=role,
                message=message
            )
        )

        db.commit()

    finally:
        db.close()