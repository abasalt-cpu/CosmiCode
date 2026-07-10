from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


main_menu = ReplyKeyboardMarkup(

    keyboard=[

        [
            KeyboardButton(text="✨ محاسبه کد کیهانی")
        ],

        [
            KeyboardButton(text="📄 گزارش من"),
            KeyboardButton(text="👤 پروفایل")
        ],

        [
            KeyboardButton(text="📚 سوابق"),
            KeyboardButton(text="ℹ️ درباره")
        ],

        [
            KeyboardButton(text="☎️ پشتیبانی")
        ]

    ],

    resize_keyboard=True

)