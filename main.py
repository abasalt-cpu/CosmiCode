from app.core import logger

logger.info("Starting CosmiCodeBot...")
import asyncio

from aiogram import Dispatcher

from app.bot import router
from app.core.bot import bot

from app.database.database import initialize_database

initialize_database()

async def main() -> None:
    dp = Dispatcher()

    dp.include_router(router)

    print("🚀 CosmiCodeBot Started...")

    await dp.start_polling(bot)
logger.info("Bot is running...")
if __name__ == "__main__":
    asyncio.run(main())