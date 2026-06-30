from sqlalchemy import text

from core.database import engine


def save_message(user_id: str, role: str, content: str):

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO memory(user_id, role, content)
                VALUES (:user_id, :role, :content)
            """),
            {
                "user_id": user_id,
                "role": role,
                "content": content
            }
        )


def get_history(user_id: str, limit: int = 20):

    with engine.begin() as conn:

        result = conn.execute(
            text("""
                SELECT role, content
                FROM memory
                WHERE user_id = :user_id
                ORDER BY id DESC
                LIMIT :limit
            """),
            {
                "user_id": user_id,
                "limit": limit
            }
        )

        rows = result.fetchall()

    rows.reverse()

    return rows