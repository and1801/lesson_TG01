import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN


import keyboards4 as kb4


bot = Bot(token=TOKEN)
dp = Dispatcher()





@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer("Опции", reply_markup=await kb4.test_keyboard())

@dp.callback_query(lambda c: c.data == 'option_1')
async def process_option_1(callback_query: CallbackQuery):
    await callback_query.answer("Вы выбрали Опцию 1")
    await callback_query.message.edit_text("Вы выбрали Опцию 1")

@dp.callback_query(lambda c: c.data == 'option_2')
async def process_option_2(callback_query: CallbackQuery):
    await callback_query.answer("Вы выбрали Опцию 2")
    await callback_query.message.edit_text("Вы выбрали Опцию 2")


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())