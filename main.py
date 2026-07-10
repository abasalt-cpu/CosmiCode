import asyncio

from aiogram import Dispatcher

from app.bot import router
from app.core.bot import bot


async def main() -> None:
    dp = Dispatcher()

    dp.include_router(router)

    print("🚀 CosmiCodeBot Started...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())