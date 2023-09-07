from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

keyboard=InlineKeyboardMarkup(row_width=True)
btn1=InlineKeyboardButton(text='🕍 Buxoro',callback_data='Buxoro')
btn2=InlineKeyboardButton(text='🕌 Andijon',callback_data='Andijon')
btn3=InlineKeyboardButton(text='🕍 Fargʻona',callback_data='Fargʻona')
btn4=InlineKeyboardButton(text='🕌 Jizzax',callback_data='Jizzax')
btn5=InlineKeyboardButton(text='🕍 Xorazm',callback_data='Namangan')
btn6=InlineKeyboardButton(text='🕌 Navoiy',callback_data='Navoiy')
btn0=InlineKeyboardButton(text='📖 menu',callback_data='menu')
btn00=InlineKeyboardButton(text='⏭ keyingisi',callback_data='keyin')
keyboard.row(btn1,btn2)
keyboard.row(btn3,btn4)
keyboard.row(btn5,btn6)
keyboard.row(btn0,btn00)
#1-bosqich

keyboard2=InlineKeyboardMarkup(row_width=True)
btn7=InlineKeyboardButton(text='🕍 Qashqadaryo',callback_data='Qashqadaryo')
btn8=InlineKeyboardButton(text='🕌 Sirdaryo',callback_data='Sirdaryo')
btn9=InlineKeyboardButton(text='🕍 Samarqand',callback_data='Samarqand')
btn10=InlineKeyboardButton(text='🕌 Toshkent',callback_data='Toshkent')
btn11=InlineKeyboardButton(text='🕍 Surxondaryo',callback_data='Surxondaryo')
btn12=InlineKeyboardButton(text='🕌 Namangan',callback_data='Namangan')
btn101=InlineKeyboardButton(text='⏮ortga',callback_data='orqaga')
btn102=InlineKeyboardButton(text='⏭ keyingi',callback_data='keyinga')
keyboard2.row(btn7,btn10)
keyboard2.row(btn9,btn8)
keyboard2.row(btn11,btn12)
keyboard2.row(btn101,btn102)
#2-bosqich



#3-bosqich
keyboard3=InlineKeyboardMarkup(row_width=True)
btn13=InlineKeyboardButton(text='🕍Qoraqalpogʻiston Respublikasi',callback_data='btn13')

btn103=InlineKeyboardButton(text='⏮ortga',callback_data='end')
btn104=InlineKeyboardButton(text='🚫 bekor qilish',callback_data='cancel')

keyboard3.row(btn13)
keyboard3.row(btn103,btn104)


language=InlineKeyboardMarkup(row_width=3)
button1=InlineKeyboardButton(text='🇺🇸 English',callback_data='en')
button2=InlineKeyboardButton(text='🇺🇿 O\'zbekcha',callback_data='uz')
button3=InlineKeyboardButton(text='🇷🇺 Русский',callback_data='ru')
language.add(button1,button2,button3)
