import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message


TOKEN = '6661964239:AAEwG7aH7gbU-7-xQ6pjqAKsa2jqptDEYzw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello! I am a word repeater bot. Send me a message, and I will repeat the words in it.")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def repeat_words(message: types.Message):
    message_text = message.text
    repeated_text = ' '.join([word for word in message_text.split()])
    await message.reply(repeated_text)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
