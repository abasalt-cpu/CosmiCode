from datetime import datetime

from app.database.database import get_connection


def create_user(user):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (telegram_id, username, first_name, joined_at, last_seen)

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user.id,
            user.username,
            user.first_name,
            datetime.utcnow().isoformat(),
            datetime.utcnow().isoformat(),
        ),
    )

    conn.commit()
    conn.close()


def update_last_seen(user):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET last_seen=?
        WHERE telegram_id=?
        """,
        (
            datetime.utcnow().isoformat(),
            user.id,
        ),
    )

    conn.commit()
    conn.close()