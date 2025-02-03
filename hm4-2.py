import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
from googletrans import Translator

import keyboards3 as kb3



bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()



@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f"Приветики, {message.from_user.full_name}", reply_markup=await kb3.test_keyboard())


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветики, {message.from_user.full_name}", reply_markup=kb3.inline_keyboard_terst)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")






async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())