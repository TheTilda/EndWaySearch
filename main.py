from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hide_link
import endway
from config import token


bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Какую тему вы ищете?')

@dp.message_handler(content_types=['text'])
async def search(message):
    search_result = endway.search(message.text)
    print(search_result)
    if search_result is None:
        await message.reply('😢Я не нашел такую тему на endway.org')
    else:
        text = ''
        for j in range(5):
            try:
                i = search_result[j]
                if i is None:
                    break
                text += f'{hide_link("https://telegra.ph/file/4f631e29335fc75c69774.png")}▶️<a href="{i["link"]}">{i["header"]}</a>\n\n'
            except:
                break
        
        await bot.send_message(message.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)