import logging
from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.Inline_keyboard import keyboard,keyboard3,keyboard2
from keyboards.default.default_keyboard import menu,menu01,menu03
from loader import dp
from  handlers.users.Api import obhavo



@dp.callback_query_handler(text='en')
async def test(query: types.CallbackQuery):
    bols = await query.message.delete()
    await query.answer("You have selected English", show_alert=True, )
    await query.message.answer("Press the area to select the button", reply_markup=menu01)


@dp.callback_query_handler(text='uz')
async def test(query:types.CallbackQuery):
    bols = await query.message.delete()
    await query.answer("Siz O'zbek tilini tanladingiz",show_alert=True,)
    await query.message.answer("Hududni tanlang  tugmasini bosing",reply_markup=menu)


@dp.callback_query_handler(text='ru')
async def test(query: types.CallbackQuery):
    bols = await query.message.delete()
    await query.answer("Вы выбрали русский", show_alert=True, )
    await query.message.answer("Нажмите область, чтобы выбрать кнопку", reply_markup=menu03)


@dp.callback_query_handler()
async def call_answer(callback:types.CallbackQuery):
    if callback.data=='Buxoro':
        bols = await callback.message.delete()
        result = obhavo('Buxoro')
        await callback.message.answer(f'{result}')
    elif callback.data=='Andijon':
        bols = await callback.message.delete()
        result = obhavo('Andijon')
        await callback.message.answer(f'{result}')
    elif callback.data=='Fargʻona':
        bols = await callback.message.delete()
        result = obhavo('Fargʻona')
        await callback.message.answer(f'{result}')
    elif callback.data=='Jizzax':
        bols = await callback.message.delete()
        result = obhavo('Jizzax')
        await callback.message.answer(f'{result}')
    elif callback.data=='Namangan':
        bols = await callback.message.delete()
        result = obhavo('Namangan')
        await callback.message.answer(f'{result}')
    elif callback.data=='Navoiy':
        bols = await callback.message.delete()
        result = obhavo('Navoiy')
        await callback.message.answer(f'{result}')
    elif callback.data=='Qashqadaryo':
        bols = await callback.message.delete()
        result = obhavo('Qashqadaryo')
        await callback.message.answer(f'{result}')
    elif callback.data=='Sirdaryo':
        bols = await callback.message.delete()
        result = obhavo('Sirdaryo')
        await callback.message.answer(f'{result}')
    elif callback.data=='Samarqand':
        bols = await callback.message.delete()
        result = obhavo('Samarqand')
        await callback.message.answer(f'{result}')
    elif callback.data=='Toshkent':
        bols = await callback.message.delete()
        result = obhavo('Toshkent')
        await callback.message.answer(f'{result}')
    elif callback.data=='Surxondaryo':
        bols = await callback.message.delete()
        result = obhavo('Surxondaryo')
        await callback.message.answer(f'{result}')
    elif callback.data=='Namangan':
        bols = await callback.message.delete()
        result = obhavo('Namangan')
        await callback.message.answer(f'{result}')
    elif callback.data=='btn13':
        bols = await callback.message.delete()
        result = obhavo('Qoraqalpogʻiston')
        await callback.message.answer(f'{result}')



    elif callback.data=='keyin':
        bols = await callback.message.delete()
        await callback.message.answer(f'Viloyatni tanlang:',reply_markup=keyboard2)
    elif callback.data=='menu':
        bols = await callback.message.delete()
        await callback.message.answer(f"Hududni tanlang  tugmasini bosing",reply_markup=menu)
    elif callback.data=='orqaga':
        bols = await callback.message.delete()
        await callback.message.answer(f'Viloyatni tanlang:',reply_markup=keyboard)
    elif callback.data == 'keyinga':
        bols = await callback.message.delete()
        await callback.message.answer(f'Viloyatni tanlang:', reply_markup=keyboard3)
    elif callback.data=='end':
        bols = await callback.message.delete()
        await callback.message.answer(f'Viloyatni tanlang:', reply_markup=keyboard2)
    elif callback.data=='cancel':
        bols = await callback.message.delete()
        await callback.message.answer(f'Viloyatni tanlang:', reply_markup=keyboard2)


