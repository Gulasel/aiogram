

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import logging 
from config import token
from parsing import get_laptops   
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может предоставить информацию о ноутбуках с сайта Сулпак. Используйте команду /laptops для получения списка ноутбуков.")

@dp.message_handler(commands=['laptops'])
async def send_laptops(message: types.Message):
    laptops = get_laptops()
    if not laptops:
        await message.reply("Не удалось получить информацию о ноутбуках.")
        return

    response_message = ""
    for laptop in laptops:
        response_message += f"{laptop['title']}\nЦена: {laptop['price']} сом\n\n"
    
    await message.reply(response_message, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
