from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.keyboards.main_menu import get_main_menu

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    text = (
        "🌌 به CosmiCode خوش آمدید.\n\n"
        "این پروژه در حال توسعه است.\n"
        "به زودی امکان محاسبه کد کیهانی و دریافت گزارش کامل اضافه خواهد شد."
    )

    await message.answer(
        text=text,
        reply_markup=get_main_menu()
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "دستورهای موجود:\n"
        "/start\n"
        "/help"
    )