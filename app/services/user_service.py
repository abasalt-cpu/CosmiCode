from app.database.session_manager import get_session

from app.database.repositories import UserRepository


class UserService:

    def __init__(self, session):
        self.repository = UserRepository(session)

    def register(self, telegram_user):

        user = self.repository.get_by_telegram_id(
            telegram_user.id
        )

        if user is None:
            user = self.repository.create(
                telegram_user
            )

        self.repository.update_last_seen(user)

        return user