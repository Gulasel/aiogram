# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
# from config import token, pay_token
# from logging import basicConfig, INFO

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)


# start_buttons = [
#     types.KeyboardButton('Цветы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес')
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


# flower_buttons = [
#     types.KeyboardButton("Розы"),
#     types.KeyboardButton("Пионы"),
#     types.KeyboardButton("Гипсофилы"),
#     types.KeyboardButton("Ромашки"),
#     types.KeyboardButton("Лилии"),
#     types.KeyboardButton("Гвоздики"),
#     types.KeyboardButton("Назад")
# ]
# flowers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*flower_buttons)


# def create_order_buttons(flower_id):
#     return types.InlineKeyboardMarkup().add(
#         types.InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
#     )


# def create_confirmation_buttons():
#     return types.InlineKeyboardMarkup().add(
#         types.InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
#         types.InlineKeyboardButton("Отменить", callback_data='cancel_order')
#     )


# order_type_buttons = types.InlineKeyboardMarkup()
# order_type_buttons.add(types.InlineKeyboardButton("Доставка", callback_data='delivery'))
# order_type_buttons.add(types.InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
# order_type_buttons.add(types.InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# payment_buttons = types.InlineKeyboardMarkup()
# payment_buttons.add(types.InlineKeyboardButton("Оплатить", callback_data='pay'))


# user_states = {}

# # Обработчик команды /start
# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

# # Обработчик текста "Контакты"
# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer('Вот наши контакты: ')
#     await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
#     await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

# # Обработчик текста "Адрес"
# @dp.message_handler(text='Адрес')
# async def send_address(message: types.Message):
#     await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
#     await message.reply_location(40.519225, 72.812685)

# # Обработчик текста "Цветы"
# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# # Обработчик текста "Назад"
# @dp.message_handler(text='Назад')
# async def back_start(message: types.Message):
#     await start(message)

# flower_data = {
#     "Розы": [
#         {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1" , "price":500 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2" , "price":550 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.","id": "roses_3" , "price":600 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4" , "price":650 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5" , "price":700 },
#     ],
    
#     "Пионы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет.", "id": "peonies_1" , "price":600},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj54ZnmbMI0MnchTsKWVeFhW6FRinXmF5mgQ&s", "caption": "Пионы - 650 сомов за букет.", "id": "peonies_2" , "price":650 },
#         {"photo": "https://tsvetochnyybiznes.ru/upload/iblock/598/5980693b7113499296ae88bfae5bc259.jpg", "caption": "Пионы -49 шт 700 сомов за букет.", "id": "peonies_3" , "price":700 },
#         {"photo": "https://static.insales-cdn.com/images/products/1/6619/187800027/IMG_8894-1_optimized.jpg", "caption": "Пионы - белые пионы 750 сомов за букет.", "id": "peonies_4" , "price":750 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRGR4eV0rkruNXhbZU5ZVDjQ4OOlQtOnhjiA&s", "caption": "Пионы - 800 сомов за букет.", "id": "peonies_5" , "price":800 }
#     ],
#     "Гипсофилы": [
#         {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет.", "id": "gypsophila_1" , "price":400},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5yRmzkU4QC2pYQT2ygPkWewSPIeLo63x2Vw&s", "caption": "Гипсофила - 450 сомов за букет.", "id": "gypsophila_2" , "price":450 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPGHqxbtdExQma1uxxqTVCAugtLJxfuVhHUA&s", "caption": "Гипсофила - 500 сомов за букет.", "id": "gypsophila_3" , "price":500 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUTcGWRvqeG8LBMAYgI3NxqOt8xiGHoyPvbw&s", "caption": "Гипсофила - 550 сомов за букет.", "id": "gypsophila_4" , "price":550 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6fX7bGcsx6RlD-RMkavWj-PRb7iGSaUlgpA&s", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5" , "price":600 },
#     ],
#     "Ромашки": [
#         {"photo": "https://img1.goodfon.ru/wallpaper/nbig/0/2a/chamomile-flowers-spring-flower-chamomiles.jpg", "caption": "Ромашки - 300 сомов за букет.", "id": "chamomile_1" , "price":300},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoGadAr2dc2rg1WKNn-9smuc2cezJSkW7Kcg&s", "caption": "Ромашки - 350 сомов за букет.", "id": "chamomile_2" , "price":350 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSBh88I_CenJAs_qLaPUFLlT9XkCIC6o1c5A&s", "caption": "Ромашки - 400 сомов за букет.", "id": "chamomile_3" , "price":400 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4-M6clRX-Ee30G0PGoX3qg9He05H1sEJmRA&s", "caption": "Ромашки - 450 сомов за букет.", "id": "chamomile_4" , "price":450 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2itH4X5t0rwzmYlEG85NlaDbHj1p_1sIkFw&s", "caption": "Ромашки - 500 сомов за букет.", "id": "chamomile_5" , "price":500 },
#     ],
#     "Лилии": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ksQ_r9E4YPir0Kcq8PaG0ROaHLk7anKT6g&s", "caption": "Лилии - 400 сомов за букет.", "id": "lilies_1" , "price":400},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxbXebfcFOx9a20RTpajMGa4_MwOb8jBgswA&s", "caption": "Лилии - 450 сомов за букет.", "id": "lilies_2" , "price":450 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCOlREJwzDsP3tN1X3pA7lGeC6vH6XocfcwQ&s", "caption": "Лилии - 500 сомов за букет.", "id": "lilies_3" , "price":500 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZJXb1Gh5iZP5JruwVllT6T-MXxDQvTdd7kw&s", "caption": "Лилии - 550 сомов за букет.", "id": "lilies_4" , "price":550 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6QeBkt7gdN6Gg_4bbrNABG0Gh1aVtL7x8dw&s", "caption": "Лилии - 600 сомов за букет.", "id": "lilies_5" , "price":600 },
#     ],
#     "Гвоздики": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhsjHb4seEwa44Cp9cbmf0G0tTk07efhrEjw&s", "caption": "Гвоздики - 250 сомов за букет.", "id": "carnations_1" , "price":250},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1T4Dd7FEj3TpL1WjNHdpq5z5U_1s3pZxFMQ&s", "caption": "Гвоздики - 300 сомов за букет.", "id": "carnations_2" , "price":300 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5p0-kTy8pQ9SwuZ5R2I3gyCq0yV79QqtiAw&s", "caption": "Гвоздики - 350 сомов за букет.", "id": "carnations_3" , "price":350 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT43rNd7SgZ1-78vK7b5Zbxl33T83JcEQuvDg&s", "caption": "Гвоздики - 400 сомов за букет.", "id": "carnations_4" , "price":400 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMC60qHKtfLSrL3hHQ7rMgWSevI5mIqC9JMQ&s", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_5" , "price":450 },
#     ]
# }

# @dp.message_handler(lambda message: message.text in flower_data)
# async def send_flower_options(message: types.Message):
#     flower_type = message.text
#     flowers = flower_data[flower_type]
#     for flower in flowers:
#         photo_id = flower["photo"]
#         caption = flower["caption"]
#         flower_id = flower["id"]
#         price = flower["price"]
#         await bot.send_photo(
#             chat_id=message.chat.id,
#             photo=photo_id,
#             caption=caption,
#             reply_markup=create_order_buttons(flower_id)
#         )

# # Обработчик callback_query для заказа
# @dp.callback_query_handler(lambda c: c.data.startswith('order_'))
# async def order_callback(callback_query: types.CallbackQuery):
#     flower_id = callback_query.data.split('_')[1]
#     flower_type = None
#     for key, flowers in flower_data.items():
#         if any(flower['id'] == flower_id for flower in flowers):
#             flower_type = key
#             break
#     if flower_type:
#         await callback_query.message.answer(
#             f"Вы выбрали {flower_type}.\nКакой способ доставки предпочитаете?",
#             reply_markup=order_type_buttons
#         )
#     else:
#         await callback_query.message.answer("Ошибка: не удалось найти цветок.")

# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def delivery_type_callback(callback_query: types.CallbackQuery):
#     delivery_type = callback_query.data
#     user_states[callback_query.from_user.id] = {"delivery_type": delivery_type}
#     await callback_query.message.answer(
#         "Пожалуйста, подтвердите ваш заказ.",
#         reply_markup=create_confirmation_buttons()
#     )

# @dp.callback_query_handler(lambda c: c.data == 'confirm_order')
# async def confirm_order_callback(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     user_data = user_states.get(user_id, {})
#     if user_data:
#         delivery_type = user_data.get("delivery_type")
#         await callback_query.message.answer(
#             f"Ваш заказ был подтвержден. Способ доставки: {delivery_type}",
#             reply_markup=payment_buttons
#         )
#     else:
#         await callback_query.message.answer("Ошибка: нет данных для подтверждения заказа.")

# @dp.callback_query_handler(lambda c: c.data == 'pay')
# async def pay_callback(callback_query: types.CallbackQuery):
#     flower_id = callback_query.message.text.split(' ')[0].lower()
#     price = 0
#     for flower_type, flowers in flower_data.items():
#         for flower in flowers:
#             if flower['id'] == flower_id:
#                 price = flower['price']
#                 break
#         if price:
#             break

#     if price:
#         await bot.send_invoice(
#             chat_id=callback_query.from_user.id,
#             title="Оплата за цветы",
#             description=f"Оплата за цветы на сумму {price} сомов.",
#             payload="order_payload",
#             provider_token=pay_token,
#             start_parameter="test_payment",
#             currency="KGS",
#             prices=[LabeledPrice(label="Цветы", amount=price * 100)]
#         )
#     else:
#         await callback_query.message.answer("Ошибка: не удалось определить цену заказа.")

# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout_handler(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# @dp.checkout_query_handler(lambda query: True)
# async def checkout_handler(checkout_query: types.CheckoutQuery):
#     await bot.send_message(
#         chat_id=checkout_query.from_user.id,
#         text="Спасибо за покупку! Ваш заказ будет обработан."
#     )

# # Рендеринг кнопок для выбора цветка
# def create_order_buttons(flower_id):
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton(text="Заказать", callback_data=f"order_{flower_id}"))
#     return markup

# # Рендеринг кнопок для выбора способа доставки
# order_type_buttons = InlineKeyboardMarkup()
# order_type_buttons.add(InlineKeyboardButton(text="Доставка", callback_data="delivery"))
# order_type_buttons.add(InlineKeyboardButton(text="Самовывоз", callback_data="self_pickup"))

# # Рендеринг кнопок для подтверждения заказа
# def create_confirmation_buttons():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton(text="Подтвердить заказ", callback_data="confirm_order"))
#     return markup

# # Рендеринг кнопок для оплаты
# payment_buttons = InlineKeyboardMarkup()
# payment_buttons.add(InlineKeyboardButton(text="Оплатить", callback_data="pay"))

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
from config import token, pay_token
from logging import basicConfig, INFO

# Создание объекта бота и диспетчера
bot = Bot(token=token)  # Инициализируем бота с токеном из конфигурации
dp = Dispatcher(bot)  # Создаем диспетчер для обработки входящих сообщений

# Настройка логирования
basicConfig(level=INFO)  # Настройка уровня логирования для отображения информационных сообщений

# Кнопки для главного меню
start_buttons = [
    types.KeyboardButton('Цветы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)  # Создание клавиатуры с кнопками главного меню

# Кнопки для выбора типа цветов
flower_buttons = [
    types.KeyboardButton("Розы"),
    types.KeyboardButton("Пионы"),
    types.KeyboardButton("Гипсофилы"),
    types.KeyboardButton("Ромашки"),
    types.KeyboardButton("Лилии"),
    types.KeyboardButton("Гвоздики"),
    types.KeyboardButton("Назад")
]
flowers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*flower_buttons)  # Клавиатура для выбора типа цветов

# Создание кнопок для заказа цветка
def create_order_buttons(flower_id):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
    )

# Кнопки для выбора типа получения заказа
order_type_buttons = InlineKeyboardMarkup()
order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# Хранение состояний пользователей
user_states = {}  # Словарь для хранения состояния пользователя

# Обработка команды /start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

# Обработка кнопки "Контакты"
@dp.message_handler(text='Контакты')
async def contact(message: types.Message):
    await message.answer('Вот наши контакты: ')
    await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
    await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

# Обработка кнопки "Адрес"
@dp.message_handler(text='Адрес')
async def send_address(message: types.Message):
    await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
    await message.reply_location(40.519225, 72.812685)

# Обработка кнопки "Цветы"
@dp.message_handler(text='Цветы')
async def send_flowers(message: types.Message):
    await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# Обработка кнопки "Назад"
@dp.message_handler(text='Назад')
async def back_start(message: types.Message):
    await start(message)

# Данные о цветах
flower_data = {
    "Розы": [
        {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1" , "price":500 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2" , "price":550 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.","id": "roses_3" , "price":600 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4" , "price":650 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5" , "price":700 },
    ],
    # Данные для других видов цветов будут добавлены аналогичным образом
}

# Обработка выбора типа цветов
@dp.message_handler(lambda message: message.text in flower_data.keys())
async def handle_flower_choice(message: types.Message):
    flower_type = message.text  # Определяем тип цветов, выбранный пользователем
    flower_list = flower_data.get(flower_type)  # Получаем данные для выбранного типа цветов
    
    if flower_list:
        for flower in flower_list:
            await bot.send_photo(message.chat.id, flower['photo'], caption=flower['caption'], reply_markup=create_order_buttons(flower['id']))
    else:
        await message.reply("Ошибка: не удалось найти данные о цветке.")

# Обработка нажатия на кнопку "Заказать"
@dp.callback_query_handler(lambda c: c.data.startswith('order_'))
async def handle_order(callback_query: types.CallbackQuery):
    flower_id = callback_query.data.split('_', 1)[1]  # Извлекаем ID выбранного букета
    user_id = callback_query.from_user.id  # Получаем ID пользователя
    
    # Сохранение состояния пользователя
    user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
    await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
    await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)

# Обработка выбора способа получения заказа
@dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
async def handle_order_type(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    order_type = callback_query.data
    
    # Обновляем состояние пользователя
    if user_id in user_states:
        user_states[user_id]['order_type'] = order_type
    
    await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
    
    if order_type == 'delivery':
        # Запрашиваем контактные данные и адрес при доставке
        await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона и адрес.",
                               reply_markup=types.ReplyKeyboardMarkup(
                                   resize_keyboard=True,
                                   one_time_keyboard=True
                               ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
        user_states[user_id]['status'] = 'awaiting_contact'
    elif order_type == 'self_pickup':
        # Сообщаем о самовывозе
        await bot.send_message(user_id, "Вы выбрали самовывоз. Ваш заказ готов к самовывозу. Спасибо!")
        del user_states[user_id]  # Завершаем сессии пользователя, так как заказ завершен

# Обработка получения контактных данных
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def handle_contact(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_contact':
        contact = message.contact
        phone_number = contact.phone_number
        
        # Запрашиваем адрес
        await bot.send_message(user_id, "Пожалуйста, укажите ваш адрес.")
        user_states[user_id]['status'] = 'awaiting_address'
        user_states[user_id]['contact'] = phone_number

# Обработка получения адреса
@dp.message_handler(lambda message: user_states.get(message.from_user.id, {}).get('status') == 'awaiting_address')
async def handle_address(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_address':
        address = message.text
        
        # Запрашиваем оплату
        flower_id = user_states[user_id].get('flower_id')
        flower_name = None
        price = None

        # Находим название и цену букета по его ID
        for flower_category in flower_data.values():
            for flower in flower_category:
                if flower['id'] == flower_id:
                    flower_name = flower['caption']
                    price = flower['price']
                    break
            if flower_name:
                break

        if price is not None:
            price_cents = price * 100  # Переводим цену в копейки
            try:
                await bot.send_invoice(
                    chat_id=user_id,
                    title=flower_name,
                    description="Оплата за заказанный букет.",
                    payload=f"flower_{flower_id}",
                    provider_token=pay_token,
                    start_parameter="test_bot",
                    currency="RUB",
                    prices=[LabeledPrice(label=flower_name, amount=price_cents)]
                )
                # Отправляем инвойс для оплаты
                await bot.send_message(user_id, "Пожалуйста, завершите оплату.")
                user_states[user_id]['status'] = 'awaiting_confirmation'
                user_states[user_id]['address'] = address
            except Exception as e:
                print(f"Ошибка при отправке инвойса: {e}")
                await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
        else:
            await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
    else:
        await bot.send_message(user_id, "Пожалуйста, сначала выберите способ получения заказа.")

@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Обработка успешной оплаты
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
        await message.answer("Оплата прошла успешно. Спасибо за ваш заказ!")
        del user_states[user_id]
    else:
        await message.answer("Не удалось подтвердить ваш заказ. Пожалуйста, попробуйте снова.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
