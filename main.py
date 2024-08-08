from aiogram import Bot, Dispatcher, executor, types
import endway
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
   await message.reply('Какую тему вы ищете?')

@dp.message_handler(content_types=['text'])
async def search(message):
   endway.search(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)