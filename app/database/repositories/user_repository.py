from datetime import datetime

from sqlalchemy import select

from app.database.models.user import User


class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_by_telegram_id(self, telegram_id: int):

        stmt = select(User).where(
            User.telegram_id == telegram_id
        )

        return self.session.scalar(stmt)

    def create(self, tg_user):

        user = User(

            telegram_id=tg_user.id,

            username=tg_user.username,

            first_name=tg_user.first_name,

            joined_at=datetime.utcnow(),

            last_seen=datetime.utcnow()

        )

        self.session.add(user)

        self.session.commit()

        return user

    def update_last_seen(self, user: User):

        user.last_seen = datetime.utcnow()

        self.session.commit()