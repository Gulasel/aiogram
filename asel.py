from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
from config import token, pay_token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)


start_buttons = [
    types.KeyboardButton('Цветы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


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


def create_order_buttons(flower_id):
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
    )
    
    
def create_confirmation_buttons():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
        types.InlineKeyboardButton("Отменить", callback_data='cancel_order')
    )


order_type_buttons = types.InlineKeyboardMarkup()
order_type_buttons.add(types.InlineKeyboardButton("Доставка", callback_data='delivery'))
order_type_buttons.add(types.InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
order_type_buttons.add(types.InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

payment_buttons = types.InlineKeyboardMarkup()
payment_buttons.add(types.InlineKeyboardButton("Оплатить", callback_data='pay'))



user_states = {}


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

@dp.message_handler(text='Цветы')
async def send_flowers(message: types.Message):
    await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

@dp.message_handler(text='Назад')
async def back_start(message: types.Message):
    await start(message)


flower_data = {
    "Розы": [
        {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1" , "price":500 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2" , "price":550 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.","id": "roses_3" , "price":600 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4" , "price":650 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5" , "price":700 },
         
    ],
    
        "Пионы": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет.", "id": "peonies_1" , "price":600},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj54ZnmbMI0MnchTsKWVeFhW6FRinXmF5mgQ&s", "caption": "Пионы - 650 сомов за букет.", "id": "peonies_2" , "price":650 },
        {"photo": "https://tsvetochnyybiznes.ru/upload/iblock/598/5980693b7113499296ae88bfae5bc259.jpg", "caption": "Пионы -49 шт 700 сомов за букет.", "id": "peonies_3" , "price":700 },
        {"photo": "https://static.insales-cdn.com/images/products/1/6619/187800027/IMG_8894-1_optimized.jpg", "caption": "Пионы - белые пионы 750 сомов за букет.", "id": "peonies_4" , "price":750 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRGR4eV0rkruNXhbZU5ZVDjQ4OOlQtOnhjiA&s", "caption": "Пионы - 800 сомов за букет.", "id": "peonies_5" , "price":800 }
    ],
    "Гипсофилы": [
        {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет.", "id": "gypsophila_1" , "price":400},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5yRmzkU4QC2pYQT2ygPkWewSPIeLo63x2Vw&s", "caption": "Гипсофила - 450 сомов за букет.", "id": "gypsophila_2" , "price":450 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPGHqxbtdExQma1uxxqTVCAugtLJxfuVhHUA&s", "caption": "Гипсофила - 500 сомов за букет.", "id": "gypsophila_3" , "price":500 },
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUTcGWRvqeG8LBMAYgI3NxqOt8xiGHoyPvbw&s", "caption": "Гипсофила - 550 сомов за букет.", "id": "gypsophila_4" , "price":550},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5" , "price":600}
    ],
    "Ромашки": [
        {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет.", "id": "daisies_1" , "price":350},
        {"photo": "https://flowercube.ru/wa-data/public/shop/products/20/07/720/images/1101/1101.750x0.jpg", "caption": "Ромашки - 400 сомов за букет.", "id": "daisies_2" , "price":400},
        {"photo": "https://camellia-market.com.ua/image/cache/catalog/3.11/51roma-auto_width_1333.jpg", "caption": "Ромашки - 450 сомов за букет.", "id": "daisies_3" , "price":450},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQySqfihDtiQV_LEwVIYwdysaxsq8vywr0OeQ&s", "caption": "Ромашки - 500 сомов за букет.", "id": "daisies_4" , "price":500},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7UxUmlq3kNPMSgFmcHXPIrMdxC0fogCPY4A&s", "caption": "Ромашки - 550 сомов за букет.", "id": "daisies_5" , "price":550}
    ],
    "Лилии": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo-aoF9xAj_hai3F1omYPGTGiJCN3XfPhkWA&s", "caption": "Лилии - 700 сомов за букет.", "id": "lilies_1" , "price":700},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_dI-l1576Y6pd20GEoUQvBzDtsVkcaZfbvQ&s", "caption": "Лилии - 750 сомов за букет.", "id": "lilies_2" , "price":750},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ4Dqf319PDX_fu-MYb-vXr0_VRrN9UHFbgw&s", "caption": "Лилии - 800 сомов за букет.", "id": "lilies_3" , "price":800},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0IPgE2E1_egaYicJ1dMA1H13tWoCwfYGGdQ&s", "caption": "Лилии - 850 сомов за букет.", "id": "lilies_4" , "price":850},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRQrLUPHfza9LeCy3G0qkMM-kR67bJAbIWVw&s", "caption": "Лилии - 900 сомов за букет.", "id": "lilies_5" , "price":900}
    ],
    "Гвоздики": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKQ0bxGV70tJ_ODDanGNtSUfg3crBXtiQVCw&s", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_1" , "price":450},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE7xV-MwYlmLB8QC-oL9vfZtYQaZJo-zGV1Q&s", "caption": "Гвоздики - 500 сомов за букет.", "id": "carnations_2" , "price":500},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIS5rq1ny3x7tOR4w2vwghPhFvf8PthAvSnA&s", "caption": "Гвоздики - 550 сомов за букет.", "id": "carnations_3" , "price":550},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQMC9Ri1nJ1_n7clHHM5So_4huntEllDwxrA&s", "caption": "Гвоздики - 600 сомов за букет.", "id": "carnations_4" , "price":600},
    ]
   
}

@dp.message_handler(text=[flower for flower in flower_data.keys()])
async def send_flower_options(message: types.Message):
    flower_name = message.text
    if flower_name in flower_data:
        for flower in flower_data[flower_name]:
            photo = flower["photo"]
            caption = flower["caption"]
            flower_id = flower["id"]
            keyboard = create_order_buttons(flower_id)
            await message.answer_photo(photo=photo, caption=caption, reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('order_'))
async def order(callback_query: types.CallbackQuery):
    flower_id = callback_query.data[len('order_'):]
    user_id = callback_query.from_user.id
    user_states[user_id] = {'status': 'awaiting_order_type', 'flower_id': flower_id}
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Выберите способ получения:", reply_markup=order_type_buttons)

@dp.callback_query_handler(lambda c: c.data == 'delivery')
async def process_delivery(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_states[user_id]['status'] = 'awaiting_phone'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=callback_query.message.message_id, reply_markup=None)

@dp.callback_query_handler(lambda c: c.data == 'self_pickup')
async def process_self_pickup(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjgL7lnpaqL56gWkHg0-RqZcUzRzAJHwr1gQ&s")
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=callback_query.message.message_id, reply_markup=None)

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


            
executor.start_polling(dp, skip_updates=True)
