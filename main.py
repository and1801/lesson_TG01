import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, OPENWEATHERMAP_API_KEY
import requests
from gtts import gTTS
import os
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

import random

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile("video.mp4")
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('sample.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('TG02.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('audio'))
async def audio(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    audio = FSInputFile("sound.mp3")
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f'Это ваша тренировка на сегодня {rand_tr}')

    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, audio)
    os.remove('training.ogg')


@dp.message(Command('photo', prefix='&'))
async def photo(message: Message):
    list = ['https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Zunge_raus.JPG/800px-Zunge_raus.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Iris_cat.jpg/200px-Iris_cat.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Domestic_cat.jpg/200px-Domestic_cat.jpg'
    ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветики, {message.from_user.full_name}")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")


@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.photo)
async def aitext(message: Message):
    list = ['Ого, какая фотка!', 'Фуу, что это?!', 'Не отправляй это никому!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

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

@dp.message()
async def translate_text(message: Message):
    # Переводим текст на английский
    try:
        translation = translator.translate(message.text, dest='en')
        await message.answer(f"Перевод на английский: {translation.text}")
    except Exception as e:
        await message.answer(f"Ошибка перевода: {e}")

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'тест':
        await message.answer('тестируем')

    await message.send_copy(chat_id=message.chat.id)



async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())