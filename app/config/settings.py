import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    PROJECT_NAME: str = "CosmiCode"

    VERSION: str = "0.4.0-dev2"


settings = Settings()