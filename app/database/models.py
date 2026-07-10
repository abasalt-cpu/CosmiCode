from dataclasses import dataclass


@dataclass
class User:

    telegram_id: int
    username: str
    first_name: str
    joined_at: str
    last_seen: str