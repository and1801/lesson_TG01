from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_keyboard_terst = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text="Показать больше", callback_data='dynamic')],

])

options = [("Опция 1", "option_1"), ("Опция 2", "option_2")]

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for text, callback_data in options:
        keyboard.add(types.InlineKeyboardButton(text=text, callback_data=callback_data))
    return keyboard.adjust(2).as_markup()