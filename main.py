import asyncio
from aiogram import Dispatcher

from app.bot import router
from app.core.bot import bot
from app.core import logger
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

async def main():
    dp=Dispatcher()
    dp.include_router(router)
    logger.info("Bot is running...")
    await dp.start_polling(bot)

if __name__=="__main__":
    logger.info("Starting CosmiCodeBot...")
    asyncio.run(main())
