from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.database.users import create_user, update_last_seen

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    create_user(message.from_user)
    update_last_seen(message.from_user)

    await message.answer(
        """
🌌 به CosmiCodeBot خوش آمدید.

این ربات کد کیهانی شما را محاسبه کرده،
تحلیل کامل شخصیت،
استعدادها،
چرخه‌های زندگی
و گزارش اختصاصی ارائه می‌کند.

برای شروع یکی از گزینه‌های زیر را انتخاب کنید.
"""
    )