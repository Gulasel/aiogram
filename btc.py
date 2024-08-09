from aiogram import Bot,Dispatcher,types,executor
from logging import basicConfig,INFO
from config import token
from aiogram.types import BotCommand
import requests,time,aioschedule

bot=Bot(token=token)
dp=Dispatcher(bot)
basicConfig(level=INFO)

async def get_btc_price():
    url='https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response=requests.get(url=url).json()
    price=response.get('price')
    if price:
        return f'Стоимость биткоина на {time.ctime()},{price}$'
    else:
        return f'Не удалось получить цену биткоина'
    
async def schedule():
    while monitoring:
        message = await get_btc_price()
        await bot.send_message(chat_id, message)
        
@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f" Привет{message.from_user.full_name}" )
    
@dp.message_handler(commands='btc')
async def btc(message:types.Message):
    global monitoring, chat_id
    chat_id=message.chat.id
    monitoring=True
    await message.answer("Начало мониторинга...")
    await schedule()
    
@dp.message_handler(commands='stop')
async def stop(message:types.Message):
    global monitoring
    monitoring=False
    await message.answer("Мониторинга цены останавлен")
    
async def on(dp):
    aioschedule.every(1).seconds.do(schedule)
 
executor.start_polling(dp,on_startup=on, skip_updates=True)


