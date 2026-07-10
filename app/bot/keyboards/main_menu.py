from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu():

    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="🧮 محاسبه کد کیهانی")
    )

    builder.row(
        KeyboardButton(text="📄 گزارش من"),
        KeyboardButton(text="👤 پروفایل")
    )

    builder.row(
        KeyboardButton(text="📜 سوابق"),
        KeyboardButton(text="ℹ️ درباره ربات")
    )

    builder.row(
        KeyboardButton(text="☎️ پشتیبانی")
    )

    return builder.as_markup(
        resize_keyboard=True
    )