import aiogram.types
from aiogram.types import Message
from aiogram import Dispatcher,types
from keyboards.default.default_keyboard import lang,menu,menu01,menu03
from keyboards.inline.Inline_keyboard import keyboard,language
from loader import dp

from keyboards.default.default_keyboard import menu


@dp.message_handler()
async def menuhandler(msg:types.Message):
    if msg.text=='🕹 Hududni tanlang':
        bols = await msg.delete()
        await msg.answer(f"Hududni tanlang",reply_markup=keyboard)
        await msg.answer(f'',reply_markup=types.ReplyKeyboardRemove(menu))

    elif msg.text=='🕹 Select the area':
        bols = await msg.delete()
        await msg.answer(f"Bot is being installed........................\n"
                         f"Please select the 🇺🇿 Uzbek language",reply_markup=language)



    elif msg.text=='🕹 Выберите область':
        await msg.answer(f"Установлен бот...............................\n"
                         f"Пожалуйста, выберите 🇺🇿 Узбекский язык",reply_markup=language)



#language
@dp.message_handler()
async def lang_default(msg:types.Message):
    if msg.text=='🇺🇿 O\'zbekcha':
        await msg.answer(f"Hududni tanlang  tugmasini bosing",reply_markup=menu)
    elif msg.text=='🇺🇸 English':
        await msg.answer(f"Press the area to select the button", reply_markup=menu01)
    elif msg.text=='🇷🇺 Русский':
        await msg.answer(f"Нажмите область, чтобы выбрать кнопку", reply_markup=menu03)

    #elif msg.text=='🔙 ortga':
       # await msg.answer(f"<b>👋  Assalomu alaykum \n\n</b>"
                           #  f"👤:<b>{msg.from_user.full_name}!\n\n</b>"
                            # f"<b>🎙 Iltimos tilni tanlang: 🇺🇿 O'zbek\n\n</b>"
                            # f"<b>🎙 Choose the language: 🇺🇸 English\n\n</b>"
                            # f"<b>🎙 Выберите язык: 🇷🇺 Русский</b>\n\n",reply_markup=language)

   # elif msg.text=='🔙 back':
      #  await msg.answer(f"<b>👋  Assalomu alaykum \n\n</b>"
               #              f"👤:<b>{msg.from_user.full_name}!\n\n</b>"
               #              f"<b>🎙 Iltimos tilni tanlang: 🇺🇿 O'zbek\n\n</b>"
                #             f"<b>🎙 Choose the language: 🇺🇸 English\n\n</b>"
                 #            f"<b>🎙 Выберите язык: 🇷🇺 Русский</b>\n\n",reply_markup=language)

   # elif msg.text=='🔙 назад':
        #await msg.answer(f"<b>👋  Assalomu alaykum \n\n</b>"
                        #     f"👤:<b>{msg.from_user.full_name}!\n\n</b>"
                        #     f"<b>🎙 Iltimos tilni tanlang: 🇺🇿 O'zbek\n\n</b>"
                         #    f"<b>🎙 Choose the language: 🇺🇸 English\n\n</b>"
                         #    f"<b>🎙 Выберите язык: 🇷🇺 Русский</b>\n\n",reply_markup=language)








