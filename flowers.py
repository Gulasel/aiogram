# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# from logging import basicConfig, INFO

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)

# # Основные кнопки
# start_buttons = [
#     types.KeyboardButton('Цветы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес'),
# ]

# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer('Вот наши контакты: ')
#     await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
#     await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

# @dp.message_handler(text='Адрес')
# async def send_address(message: types.Message):
#     await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
#     await message.reply_location(40.519225, 72.812685)

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

# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# # Данные о цветах
# flower_data = {
#     "Розы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0Q_5SpT9IfXHLHxejtvPebXWK2oJ2t5QjQQ&s", "caption": "Розы - 500 сомов за букет."},
#         {"photo": "https://i5.stat01.com/2/4018/140173607/afacdb/buket-iz-pionovidnyh-roz-bombastik.jpg", "caption": "Розы - 550 сомов за букет."},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT6XdVukW2PCyHhWnkFMw9N6cN81XSNX_Jeg&s", "caption": "Розы - 600 сомов за букет."},
#         {"photo": "https://www.roza4u.ru/image/cache/catalog/101-red-40sm/IMG_3039-1400x1400.jpg", "caption": "Розы - 650 сомов за букет."},
#         {"photo": "https://gorod-buketov.ru/wp-content/uploads/2017/04/54911-8-800-min.jpeg", "caption": "Розы - 700 сомов за букет."}
#     ],
#     "Пионы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет."},
#         {"photo": "https://example.com/peonies2.jpg", "caption": "Пионы - 650 сомов за букет."},
#         {"photo": "https://example.com/peonies3.jpg", "caption": "Пионы - 700 сомов за букет."},
#         {"photo": "https://example.com/peonies4.jpg", "caption": "Пионы - 750 сомов за букет."},
#         {"photo": "https://example.com/peonies5.jpg", "caption": "Пионы - 800 сомов за букет."}
#     ],
#     "Гипсофилы": [
#         {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет."},
#         {"photo": "https://example.com/gypsophila2.jpg", "caption": "Гипсофила - 450 сомов за букет."},
#         {"photo": "https://example.com/gypsophila3.jpg", "caption": "Гипсофила - 500 сомов за букет."},
#         {"photo": "https://example.com/gypsophila4.jpg", "caption": "Гипсофила - 550 сомов за букет."},
#         {"photo": "https://example.com/gypsophila5.jpg", "caption": "Гипсофила - 600 сомов за букет."}
#     ],
#     "Ромашки": [
#         {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет."},
#         {"photo": "https://example.com/daisies2.jpg", "caption": "Ромашки - 400 сомов за букет."},
#         {"photo": "https://example.com/daisies3.jpg", "caption": "Ромашки - 450 сомов за букет."},
#         {"photo": "https://example.com/daisies4.jpg", "caption": "Ромашки - 500 сомов за букет."},
#         {"photo": "https://example.com/daisies5.jpg", "caption": "Ромашки - 550 сомов за букет."}
#     ],
#     "Лилии": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo-aoF9xAj_hai3F1omYPGTGiJCN3XfPhkWA&s", "caption": "Лилии - 700 сомов за букет."},
#         {"photo": "https://example.com/lilies2.jpg", "caption": "Лилии - 750 сомов за букет."},
#         {"photo": "https://example.com/lilies3.jpg", "caption": "Лилии - 800 сомов за букет."},
#         {"photo": "https://example.com/lilies4.jpg", "caption": "Лилии - 850 сомов за букет."},
#         {"photo": "https://example.com/lilies5.jpg", "caption": "Лилии - 900 сомов за букет."}
#     ],
#     "Гвоздики": [
#         {"photo": "https://example.com/carnations.jpg", "caption": "Гвоздики - 450 сомов за букет."},
#         {"photo": "https://example.com/carnations2.jpg", "caption": "Гвоздики - 500 сомов за букет."},
#         {"photo": "https://example.com/carnations3.jpg", "caption": "Гвоздики - 550 сомов за букет."},
#         {"photo": "https://example.com/carnations4.jpg", "caption": "Гвоздики - 600 сомов за букет."},
#         {"photo": "https://example.com/carnations5.jpg", "caption": "Гвоздики - 650 сомов за букет."}
#     ]
# }

# @dp.message_handler(text=[key for key in flower_data.keys()])
# async def send_flower_options(message: types.Message):
#     flower_name = message.text
#     if flower_name in flower_data:
#         media_group = [types.InputMediaPhoto(media=flower["photo"], caption=flower["caption"]) for flower in flower_data[flower_name]]
#         await message.answer_media_group(media=media_group)

# @dp.message_handler(text="Назад")
# async def back_start(message: types.Message):
#     await start(message)

# executor.start_polling(dp, skip_updates=True)





# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# from logging import basicConfig, INFO

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)

# # Основные кнопки
# start_buttons = [
#     types.KeyboardButton('Цветы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес'),
# ]

# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer('Вот наши контакты: ')
#     await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
#     await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

# @dp.message_handler(text='Адрес')
# async def send_address(message: types.Message):
#     await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
#     await message.reply_location(40.519225, 72.812685)

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

# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# # Данные о цветах
# flower_data = {
#     "Розы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0Q_5SpT9IfXHLHxejtvPebXWK2oJ2t5QjQQ&s", "caption": "Розы - 500 сомов за букет."},
#         {"photo": "https://i5.stat01.com/2/4018/140173607/afacdb/buket-iz-pionovidnyh-roz-bombastik.jpg", "caption": "Розы - 550 сомов за букет."},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT6XdVukW2PCyHhWnkFMw9N6cN81XSNX_Jeg&s", "caption": "Розы - 600 сомов за букет."},
#         {"photo": "https://www.roza4u.ru/image/cache/catalog/101-red-40sm/IMG_3039-1400x1400.jpg", "caption": "Розы - 650 сомов за букет."},
#         {"photo": "https://gorod-buketov.ru/wp-content/uploads/2017/04/54911-8-800-min.jpeg", "caption": "Розы - 700 сомов за букет."}
      
#     ],
#     "Пионы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет."},
#         {"photo": "https://example.com/peonies2.jpg", "caption": "Пионы - 650 сомов за букет."},
#         {"photo": "https://example.com/peonies3.jpg", "caption": "Пионы - 700 сомов за букет."},
#         {"photo": "https://example.com/peonies4.jpg", "caption": "Пионы - 750 сомов за букет."},
#         {"photo": "https://example.com/peonies5.jpg", "caption": "Пионы - 800 сомов за букет."}
#     ],
#     "Гипсофилы": [
#         {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет."},
#         {"photo": "https://example.com/gypsophila2.jpg", "caption": "Гипсофила - 450 сомов за букет."},
#         {"photo": "https://example.com/gypsophila3.jpg", "caption": "Гипсофила - 500 сомов за букет."},
#         {"photo": "https://example.com/gypsophila4.jpg", "caption": "Гипсофила - 550 сомов за букет."},
#         {"photo": "https://example.com/gypsophila5.jpg", "caption": "Гипсофила - 600 сомов за букет."}
#     ],
#     "Ромашки": [
#         {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет."},
#         {"photo": "https://example.com/daisies2.jpg", "caption": "Ромашки - 400 сомов за букет."},
#         {"photo": "https://example.com/daisies3.jpg", "caption": "Ромашки - 450 сомов за букет."},
#         {"photo": "https://example.com/daisies4.jpg", "caption": "Ромашки - 500 сомов за букет."},
#         {"photo": "https://example.com/daisies5.jpg", "caption": "Ромашки - 550 сомов за букет."}
#     ],
#     "Лилии": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo-aoF9xAj_hai3F1omYPGTGiJCN3XfPhkWA&s", "caption": "Лилии - 700 сомов за букет."},
#         {"photo": "https://example.com/lilies2.jpg", "caption": "Лилии - 750 сомов за букет."},
#         {"photo": "https://example.com/lilies3.jpg", "caption": "Лилии - 800 сомов за букет."},
#         {"photo": "https://example.com/lilies4.jpg", "caption": "Лилии - 850 сомов за букет."},
#         {"photo": "https://example.com/lilies5.jpg", "caption": "Лилии - 900 сомов за букет."}
#     ],
#     "Гвоздики": [
#         {"photo": "https://example.com/carnations.jpg", "caption": "Гвоздики - 450 сомов за букет."},
#         {"photo": "https://example.com/carnations2.jpg", "caption": "Гвоздики - 500 сомов за букет."},
#         {"photo": "https://example.com/carnations3.jpg", "caption": "Гвоздики - 550 сомов за букет."},
#         {"photo": "https://example.com/carnations4.jpg", "caption": "Гвоздики - 600 сомов за букет."},
#         {"photo": "https://example.com/carnations5.jpg", "caption": "Гвоздики - 650 сомов за букет."}
#     ]
# }

# @dp.message_handler(text=[key for key in flower_data.keys()])
# async def send_flower_options(message: types.Message):
#     flower_name = message.text
#     if flower_name in flower_data:
#         for flower in flower_data[flower_name]:
#             await message.answer_photo(photo=flower["photo"], caption=flower["caption"])

# @dp.message_handler(text="Назад")
# async def back_start(message: types.Message):
#     await start(message)

# executor.start_polling(dp, skip_updates=True)



from aiogram import Bot, Dispatcher, types, executor
from config import token , pay_token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

# Основные кнопки
start_buttons = [
    types.KeyboardButton('Цветы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес'),
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

@dp.message_handler(text='Контакты')
async def contact(message: types.Message):
    await message.answer('Вот наши контакты: ')
    await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
    await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

@dp.message_handler(text='Адрес')
async def send_address(message: types.Message):
    await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
    await message.reply_location(40.519225, 72.812685)

flower_buttons = [
    types.KeyboardButton("Розы"),
    types.KeyboardButton("Пионы"),
    types.KeyboardButton("Гипсофилы"),
    types.KeyboardButton("Ромашки"),
    types.KeyboardButton("Лилии"),
    types.KeyboardButton("Гвоздики"),
    types.KeyboardButton("Назад")
]
flowers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*flower_buttons)

@dp.message_handler(text='Цветы')
async def send_flowers(message: types.Message):
    await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# Данные о цветах
flower_data = {
    "Розы": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0Q_5SpT9IfXHLHxejtvPebXWK2oJ2t5QjQQ&s", "caption": "Розы - 500 сомов за букет.", "id": "roses_1"},
        {"photo": "https://i5.stat01.com/2/4018/140173607/afacdb/buket-iz-pionovidnyh-roz-bombastik.jpg", "caption": "Розы - 550 сомов за букет.", "id": "roses_2"},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT6XdVukW2PCyHhWnkFMw9N6cN81XSNX_Jeg&s", "caption": "Розы - 600 сомов за букет.", "id": "roses_3"},
        {"photo": "https://www.roza4u.ru/image/cache/catalog/101-red-40sm/IMG_3039-1400x1400.jpg", "caption": "Розы - 650 сомов за букет.", "id": "roses_4"},
        {"photo": "https://gorod-buketov.ru/wp-content/uploads/2017/04/54911-8-800-min.jpeg", "caption": "Розы - 700 сомов за букет.", "id": "roses_5"}
    ],
    "Пионы": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет.", "id": "peonies_1"},
        {"photo": "https://example.com/peonies2.jpg", "caption": "Пионы - 650 сомов за букет.", "id": "peonies_2"},
        {"photo": "https://example.com/peonies3.jpg", "caption": "Пионы - 700 сомов за букет.", "id": "peonies_3"},
        {"photo": "https://example.com/peonies4.jpg", "caption": "Пионы - 750 сомов за букет.", "id": "peonies_4"},
        {"photo": "https://example.com/peonies5.jpg", "caption": "Пионы - 800 сомов за букет.", "id": "peonies_5"}
    ],
    "Гипсофилы": [
        {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет.", "id": "gypsophila_1"},
        {"photo": "https://example.com/gypsophila2.jpg", "caption": "Гипсофила - 450 сомов за букет.", "id": "gypsophila_2"},
        {"photo": "https://example.com/gypsophila3.jpg", "caption": "Гипсофила - 500 сомов за букет.", "id": "gypsophila_3"},
        {"photo": "https://example.com/gypsophila4.jpg", "caption": "Гипсофила - 550 сомов за букет.", "id": "gypsophila_4"},
        {"photo": "https://example.com/gypsophila5.jpg", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5"}
    ],
    "Ромашки": [
        {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет.", "id": "daisies_1"},
        {"photo": "https://example.com/daisies2.jpg", "caption": "Ромашки - 400 сомов за букет.", "id": "daisies_2"},
        {"photo": "https://example.com/daisies3.jpg", "caption": "Ромашки - 450 сомов за букет.", "id": "daisies_3"},
        {"photo": "https://example.com/daisies4.jpg", "caption": "Ромашки - 500 сомов за букет.", "id": "daisies_4"},
        {"photo": "https://example.com/daisies5.jpg", "caption": "Ромашки - 550 сомов за букет.", "id": "daisies_5"}
    ],
    "Лилии": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo-aoF9xAj_hai3F1omYPGTGiJCN3XfPhkWA&s", "caption": "Лилии - 700 сомов за букет.", "id": "lilies_1"},
        {"photo": "https://example.com/lilies2.jpg", "caption": "Лилии - 750 сомов за букет.", "id": "lilies_2"},
        {"photo": "https://example.com/lilies3.jpg", "caption": "Лилии - 800 сомов за букет.", "id": "lilies_3"},
        {"photo": "https://example.com/lilies4.jpg", "caption": "Лилии - 850 сомов за букет.", "id": "lilies_4"},
        {"photo": "https://example.com/lilies5.jpg", "caption": "Лилии - 900 сомов за букет.", "id": "lilies_5"}
    ],
    "Гвоздики": [
        {"photo": "https://example.com/carnations.jpg", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_1"},
        {"photo": "https://example.com/carnations2.jpg", "caption": "Гвоздики - 500 сомов за букет.", "id": "carnations_2"},
        {"photo": "https://example.com/carnations3.jpg", "caption": "Гвоздики - 550 сомов за букет.", "id": "carnations_3"},
        {"photo": "https://example.com/carnations4.jpg", "caption": "Гвоздики - 600 сомов за букет.", "id": "carnations_4"},
        {"photo": "https://example.com/carnations5.jpg", "caption": "Гвоздики - 650 сомов за букет.", "id": "carnations_5"}
    ]
}@dp.callback_query_handler(lambda c: c.data == 'order')
async def order(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_states[user_id] = {'status': 'awaiting_order_type'}  # Установить состояние ожидания выбора типа заказа
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Выберите способ получения:", reply_markup=order_type_buttons)

@dp.callback_query_handler(lambda c: c.data == 'delivery')
async def process_delivery(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_states[user_id] = {'status': 'awaiting_phone'}
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))

@dp.callback_query_handler(lambda c: c.data == 'self_pickup')
async def process_self_pickup(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Вы выбрали самовывоз. Приходите в наш магазин по адресу: Город Ош, 275 А.Шакирова ул")

@dp.callback_query_handler(lambda c: c.data == 'back_to_flowers')
async def back_to_flowers(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Выберите вид цветов", reply_markup=flowers_keyboard)

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def handle_phone(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_phone':
        user_states[user_id]['phone'] = message.contact.phone_number
        user_states[user_id]['status'] = 'awaiting_address'
        await message.reply("Теперь укажите адрес доставки.")

@dp.message_handler(lambda message: user_states.get(message.from_user.id, {}).get('status') == 'awaiting_address')
async def handle_address(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_address':
        user_states[user_id]['address'] = message.text
        await message.reply("Адрес получен. Пожалуйста, подтвердите оплату за букет.", reply_markup=payment_buttons)
        user_states[user_id]['status'] = 'awaiting_payment'

@dp.callback_query_handler(lambda c: c.data == 'pay')
async def handle_payment(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
        # Замените параметры на ваши реальные данные
        await bot.answer_callback_query(callback_query.id)
        await bot.send_invoice(
            chat_id=user_id,
            title="Оплата за букет",
            description="Оплата за заказанный букет.",
            payload="flower",  # Используйте уникальный идентификатор платежа
            provider_token=pay_token,  # Токен вашего платёжного провайдера
            start_parameter="test_bot",
            currency="RUB",  # Введите вашу валюту
            prices=[types.LabeledPrice(label="Букет", amount=50000)]  # Укажите цену (в копейках)
        )



def create_order_button(flower_id):
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Заказать", callback_data=f"order_{flower_id}")
    )

@dp.message_handler(text=[key for key in flower_data.keys()])
async def send_flower_options(message: types.Message):
    flower_name = message.text
    if flower_name in flower_data:
        for flower in flower_data[flower_name]:
            photo = flower["photo"]
            caption = flower["caption"]
            flower_id = flower["id"]
            keyboard = create_order_button(flower_id)
            await message.answer_photo(photo=photo, caption=caption, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('order_'))
async def process_order(callback_query: types.CallbackQuery):
    flower_id = callback_query.data[len('order_'):]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        f"Ваш заказ на цветок с ID {flower_id} был принят! Мы свяжемся с вами для подтверждения."
    )

@dp.message_handler(text="Назад")
async def back_start(message: types.Message):
    await start(message)

executor.start_polling(dp, skip_updates=True)
