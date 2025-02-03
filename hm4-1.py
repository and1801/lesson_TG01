import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN


import keyboards2 as kb2


bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.callback_query(F.data == "hi")
async def hi(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(f'Привет, {callback.from_user.full_name}!')

@dp.callback_query(F.data == "bye")
async def bye(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(f'Пока, {callback.from_user.full_name}!')




@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветики, {message.from_user.full_name}", reply_markup=kb2.inline_keyboard_terst)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")




async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())