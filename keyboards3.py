from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_keyboard_terst = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
    [InlineKeyboardButton(text="Новости", callback_data='news')],
    [InlineKeyboardButton(text="Профиль", callback_data='person')]
])

buttons = [
    {"text": "Новости", "url":"https://pikabu.ru/"},
    {"text": "Музыка", "url":"https://muzofond.fm/collections/artists/%D0%B1%D0%B8%202"},
    {"text": "Видео", "url":"https://www.youtube.com/watch?v=gjzCnCM7rjM"}
    ]

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button["text"], url=button["url"]))
    return keyboard.adjust(2).as_markup()