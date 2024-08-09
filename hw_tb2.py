# from aiogram import Bot, Dispatcher, types, executor
# from logging import basicConfig, INFO


# bot = Bot(token='7011991566:AAFJreIBegl5nvCbIN8HaVtENBi56zau9Sk')
# dp = Dispatcher(bot)
# basicConfig(level=INFO)


# start_buttons = [
#     types.KeyboardButton('О нас'),
#     types.KeyboardButton('Товары'),
#     types.KeyboardButton('Заказать'),
#     types.KeyboardButton('Контакты'),
# ]age):
    
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


# products = {
#     "IPHONE": {"name": "IPhone", "description": "Серия смартфонов от Apple", "price": "120 000", "article": "7741 5425 2552",
#                "photo_url": "https://www.ixbt.com/img/n1/news/2020/11/2/281869_02_iphone_11_pro_family_large_0_large.jpg"},
#     "SAMSUNG": {"name": "Samsung", "description": "Самый лучший телефон", "price": "42 000", "article": "884755 4454 255548",
#                 "photo_url": "https://resizer.mail.ru/p/f1e84d94-4d0f-5d9d-a184-752d7ba78ff7/AQAKw2PpfGxzafbp8cKWpv6MmdSeSLTfDtrsg91S-CR6pU4tYKxIbeP_WBk_xD3amWApiQE0zgQNcsB-ipgM-JO1ZfU.png"}
# }


# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

# @dp.message_handler(text='О нас')
# async def about_us(message: types.Message):
#     await message.reply("Добро пожаловать в магазин Tehno-shop! У нас вы можете приобрести лучшие смартфоны по выгодным ценам.")


# @dp.message_handler(text='Товары')
# async def send_products(message: types.Message):
#     products_list = "\n\n".join([f"Название: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']}\n" for product in products.values()])
#     await message.reply(products_list)

# @dp.message_handler(text='Заказать')
# async def request_order(message: types.Message):
#     await message.reply("Введите артикул товара, который хотите заказать:")

# # Обработчик для получения артикула товара
# @dp.message_handler(lambda message: message.text in products.keys())
# async def process_order(message: types.Message):
#     product_name = message.text
#     product = products.get(product_name)
#     text = f"Вы выбрали товар:\nНазвание: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']}\nАртикул: {product['article']}"
#     await message.answer(text)
#     await message.answer_photo(photo=product['photo_url'])
#     await message.answer("Теперь поделитесь вашим контактом для связи (номер телефона):")


# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer(f'{message.from_user.full_name}, вот наши контакты:')
#     await message.answer_contact("+996500232632", "Гуласел", "Усеновна")
#     await message.answer_contact("+996777797921", "Элиза", "Эркинбековна")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
    
    
# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# from logging import basicConfig, INFO

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)
    
# start_buttons = [
#     types.KeyboardButton('О нас'),
#     types.KeyboardButton('Товары'),
#     types.KeyboardButton('Заказать'),
#     types.KeyboardButton('Контакты'),
# ]

# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

# @dp.message_handler(text='О нас')
# async def about_us(message: types.Message):
#     await message.reply("Добро пожаловать в магазин Tehno-shop! У нас вы можете приобрести лучшие смартфоны по выгодным ценам.")

# @dp.message_handler(text='Товары')
# async def send_products(message: types.Mess




