from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, PreCheckoutQuery, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from config import token, pay_token
import logging


bot = Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

buy_laptop_cb = CallbackData('buy', 'item_id')

@dp.message_handler(commands='start')
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук HP Victus', callback_data=buy_laptop_cb.new(item_id='laptop1')))
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук Aser', callback_data=buy_laptop_cb.new(item_id='laptop2')))
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук ASUS ', callback_data=buy_laptop_cb.new(item_id='laptop3')))
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук Lenovo ', callback_data=buy_laptop_cb.new(item_id='laptop4')))
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук Hiaomi ', callback_data=buy_laptop_cb.new(item_id='laptop5')))
    await message.reply("Привет выбери товар для покупки", reply_markup=keyboard)

@dp.callback_query_handler(buy_laptop_cb.filter())
async def process_payment(callback: CallbackQuery, callback_data: dict):
    item_id = callback_data['item_id']
    price_details = {
        'laptop1': (7000000, 'Ноутбук HP Victus 15 Gaming Laptop Intel Core i5-12500H 12th Gen/NVIDIA GeForce RTX 3050 (8+512GB SSD)', 'https://softech.kg/image/cache/7b73ce0ac5b18f69b1b012d893544de1.jpg'),
        'laptop2': (8000000, 'Ноутбук EX215-54-510N 15.6" FHD LCD i5-1135G7 8Gb 512Gb SSD', 'https://object.pscloud.io/cms/cms/Photo/img_0_62_3025_0_1_VZeASF.jpg'),
        'laptop3': (9000000, 'Ноутбук Asus ROG Strix G15 G513RM-WS74 AMD Ryzen 7 6800H 16GB DDR5 1000GB SSD Nvidia RTX3060 6GB WQHD W11', 'https://softech.kg/image/cache/7df21c6e02e152e4902cf3ce3ff6017d.jpg'),
        'laptop4': (7500000, 'Lenovo Ideapad S145-15API Silver AMD 3020e (up to 2.6Ghz), 4GB, 128GB SSD, AMD Radeon™ Graphics, 15.6″ LED, WiFi, BT, Cam, DOS', 'https://ultra.kg/upload/resize_cache/iblock/81a/1120_842_1d0e97ea46f4438969ab06dd5b311ca67/81ab6a8d128c7a79c8605695b363a81c.jpg'),
        'laptop5': (6500000, 'Ноутбук Xiaomi Mi Notebook Pro 15 OLED i5-11320H 11th Gen/GeForce MX450 (16+512GB SSD)', 'https://softech.kg/image/cache/2ad2cc88ae37852e6a5ae45d08cf63b3.jpg')
    }
    
    price, description, photo_url = price_details.get(item_id, (0, 'Описание недоступно', 'https://example.com/default.jpg'))

    price_details_list = [LabeledPrice(label=description, amount=price)]

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title=description.split()[0],  
        payload=item_id,
        description=description,
        provider_token=pay_token,
        currency='RUB',
        prices=price_details_list,
        start_parameter='test_bot',
        photo_url=photo_url,
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    await callback.answer()

@dp.pre_checkout_query_handler(lambda query: True)
async def pre(pre: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def suc(message: types.Message):
    await message.reply("Спасибо за покупку")

async def on_shutdown(dp):
    await bot.session.close()

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)
