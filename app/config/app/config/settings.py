from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class Settings:

    bot_token: str

    project_name: str

    version: str

    debug: bool

    database_url: str


def _get_bool(name: str, default: bool = False) -> bool:

    value = os.getenv(name)

    if value is None:
        return default

    return value.lower() in ("1", "true", "yes", "on")


settings = Settings(

    bot_token=os.getenv("BOT_TOKEN", ""),

    project_name="CosmiCode",

    version="0.5.0-dev1",

    debug=_get_bool("DEBUG", True),

    database_url=os.getenv(
        "DATABASE_URL",
        "sqlite:///cosmicode.db",
    ),
)