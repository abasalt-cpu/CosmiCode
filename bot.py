from aiogram import Bot
from aiogram.enums import ParseMode

from app.config.settings import settings

bot = Bot(
    token=settings.BOT_TOKEN,
    default=Bot.default.parse_mode(ParseMode.HTML)
)