from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

menu=ReplyKeyboardMarkup(resize_keyboard=True)
bnt1=KeyboardButton(text='🕹 Hududni tanlang')
bnt2=KeyboardButton(text='🔙 ortga')
menu.add(bnt1)


menu01=ReplyKeyboardMarkup(resize_keyboard=True)
bnt1=KeyboardButton(text='🕹 Select the area')
bnt2=KeyboardButton(text='🔙 back')
menu01.add(bnt1)


menu03=ReplyKeyboardMarkup(resize_keyboard=True)
bnt1=KeyboardButton(text='🕹 Выберите область')
bnt2=KeyboardButton(text='🔙 назад',)
menu03.add(bnt1)



menu2=ReplyKeyboardMarkup(resize_keyboard=True)
bnt3=KeyboardButton(text='⏭keyingi')
bnt4=KeyboardButton(text='⏮ ortga')
bnt0=KeyboardButton(text='🚫 bekor qilish')
menu2.row(bnt3,bnt4)
menu2.add(bnt0)

menu3=ReplyKeyboardMarkup(resize_keyboard=True)
bnt5=KeyboardButton(text='⏭keyingi')
bnt6=KeyboardButton(text='⏮ortga')
bnt0=KeyboardButton(text='🚫 bekor qilish')
menu3.row(bnt5,bnt6)
menu3.add(bnt0)


lang=ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
button1=KeyboardButton(text='🇺🇸 English')
button2=KeyboardButton(text='🇺🇿 O\'zbekcha')
button3=KeyboardButton(text='🇷🇺 Русский')
lang.add(button1,button2,button3)

