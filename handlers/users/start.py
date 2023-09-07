from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.default_keyboard import menu
from keyboards.inline.Inline_keyboard import keyboard,language
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>👋  Assalomu alaykum \n\n</b>"
                             f"👤:<b>{message.from_user.full_name}!\n\n</b>"
                             f"<b>🎙 Iltimos tilni tanlang: 🇺🇿 O'zbek\n\n</b>"
                             f"<b>🎙 Choose the language: 🇺🇸 English\n\n</b>"
                             f"<b>🎙 Выберите язык: 🇷🇺 Русский</b>\n\n",reply_markup=language)


