# import schedule
# import time
# import requests

# def perform_request(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Проверяет статус-код ответа
#         print(f"URL: {url} - Status Code: {response.status_code} - Response: {response.text[:200]}")  # Печатает первые 200 символов ответа
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred: {e}")

      
# def main():
#     url = "https://ru.investing.com/currencies/xau-usd"  
#     initial_delay = 5  # Начальная задержка в секундах
#     interval = 10  # Интервал между запросами в секундах


#     schedule.every(interval).seconds.do(perform_request, url)

#     print(f"Scheduled tasks to run every {interval} seconds.")
#     print(f"Initial delay before starting the scheduler: {initial_delay} seconds.")
    
#     # Ждём начальной задержки
#     time.sleep(initial_delay)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)  # Периодическое ожидание для снижения загрузки CPU




from aiogram import Bot,Dispatcher,types,executor
from logging import basicConfig,INFO
from config import token
from aiogram.types import BotCommand
import requests,time,aioschedule

bot=Bot(token=token)
dp=Dispatcher(bot)
basicConfig(level=INFO)


async def get_gold_price():
    url='https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response=requests.get(url=url).json()
    price=response.get('price')
    if price:
        return f'Стоимость золоты на {time.ctime()},{price}$'
    else:
        return f'Не удалось получить цену золоты'
    
   # https://pool.binance.com/en