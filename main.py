import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, OPENWEATHERMAP_API_KEY
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()

import random

@dp.message (CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")


@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.photo)
async def aitext(message: Message):
    list = ['Ого, какая фотка', 'Фуу, что это?!', 'Не отправляй это никому']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command('weather'))
async def weather(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите город. Например: /weather Москва")
        return

    city = args[1]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang=ru"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        await message.answer("Не удалось получить данные о погоде.")
        return

    weather_description = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]

    weather_info = (
        f"Погода в {city}:\n"
        f"Описание: {weather_description}\n"
        f"Температура: {temperature}°C\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed} м/с"
    )

    await message.answer(weather_info)


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())