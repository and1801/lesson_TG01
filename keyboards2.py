from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



inline_keyboard_terst = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Привет!", callback_data='hi')],
    [InlineKeyboardButton(text="Пока!", callback_data='bye')],
])

