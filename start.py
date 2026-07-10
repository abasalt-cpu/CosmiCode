from app.database.session import SessionLocal
from app.services import UserService
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.database.users import create_user, update_last_seen
from app.bot.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    session = SessionLocal()

service = UserService(session)

service.register(message.from_user)

session.close()
    await message.answer(
    text="🌌 به CosmiCodeBot خوش آمدید.",
    reply_markup=main_menu
)

این ربات کد کیهانی شما را محاسبه کرده،
تحلیل کامل شخصیت،
استعدادها،
چرخه‌های زندگی
و گزارش اختصاصی ارائه می‌کند.

برای شروع یکی از گزینه‌های زیر را انتخاب کنید.
"""
    )