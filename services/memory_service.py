from sqlalchemy import desc

from core.database import SessionLocal
from models.memory import Memory


def get_history(user_id: int, limit: int = 20):

    db = SessionLocal()

    try:

        rows = (
            db.query(Memory)
            .filter(Memory.user_id == user_id)
            .order_by(desc(Memory.id))
            .limit(limit)
            .all()
        )

        rows.reverse()

        history = []

        for row in rows:

            history.append({
                "role": row.role,
                "message": row.message
            })

        return history

    finally:

        db.close()