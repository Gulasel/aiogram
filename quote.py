from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from config import token
import random

bot=Bot(token=token)
dp=Dispatcher(bot)

QUOTES = [
   "Ваше время ограничено, не тратьте его, живя чужой жизнью.",
   "Победа - это еще не все, все - это постоянное желание побеждать.",
   "Либо вы управляете вашим днем, либо день управляет вами.",
   "Всё, что мы есть, — это результат наших мыслей.", 
   "Жизнь — это то, что происходит, пока ты строишь другие планы."
]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("Привет! Отправьте команду /quote, чтобы получить случайную цитату.")
    
@dp.message_handler(commands='quote')
async def quote(message: types.Message):
    quote = random.choice(QUOTES)
    await message.reply(quote)

executor.start_polling(dp, skip_updates=True)