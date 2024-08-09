# from aiogram import Bot, Dispatcher, types, executor  
# from config import token

# import requests
# from bs4 import BeautifulSoup


# bot = Bot(token=token)
# dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f'Здравствуйте, {message.from_user.full_name}!')


# @dp.message_handler(commands=['laptops'])
# async def send_laptops(message: types.Message):                      
#     def get_laptops():
#         url = 'https://www.sulpak.kg/f/noutbuki'
#         response = requests.get(url, verify=False)
#         soup = BeautifulSoup(response.text, 'html.parser')

#     laptops = []
#     product_containers = soup.select('.product__item-inner')
#     if not product_containers:
#         print("No products found. Check the selectors.")
#         return laptops

#     for item in product_containers:
#         title_element = item.select_one('.product__item-name a')
#         price_element = item.select_one('.product__item-price')
#         if title_element and price_element:
#             title = title_element.get_text(strip=True)
#             price = price_element.get_text(strip=True).replace('сом', '').strip()
#             laptops.append({
#                 'title': title,
#                 'price': price
#             })

#     return laptops

# # if __name__ == '__main__':
# #     laptops = get_laptops()
# #     if laptops:
# #         for laptop in laptops:
# #             print(f"{laptop['title']}\nЦена: {laptop['price']} сом\n")
# #     else:
# #         print("No laptops found.")




# laptop=get_laptops()
# if not laptop:
#     await message.reply("Не получилось")
#     return
# for laptop in laptops:
#     await message.reply(f'{laptop['title']}\nцена {laptop['price'] com})


# from aiogram import Bot, Dispatcher, types
# import logging 
# from config import token
# from parsing import get_laptops  



# bot = Bot(token=token)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply(f'Здравствуйте, {message.from_user.full_name}!')

# @dp.message_handler(commands=['laptops'])
# async def send_laptops(message: types.Message):
#     laptops = get_laptops()
#     if not laptops:
#         await message.reply("Не удалось получить информацию о ноутбуках.")
#         return

#     response_message = ""
#     for laptop in laptops:
#         response_message += f"{laptop['title']}\nЦена: {laptop['price']} сом\n\n"
    
#     await message.reply(response_message, parse_mode=ParseMode.MARKDOWN)

#     executor.start_polling(dp, skip_updates=True)

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
