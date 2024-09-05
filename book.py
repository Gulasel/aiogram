from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove
from config import token ,pay_token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

# Основные кнопки
start_buttons = [
    types.KeyboardButton('Цветы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# Кнопки для выбора цветов
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

# Инлайн кнопки для заказа
order_buttons = types.InlineKeyboardMarkup()
order_buttons.add(types.InlineKeyboardButton("Заказать", callback_data='order'))

# Инлайн кнопки для выбора способа получения
order_type_buttons = types.InlineKeyboardMarkup()
order_type_buttons.add(types.InlineKeyboardButton("Доставка", callback_data='delivery'))
order_type_buttons.add(types.InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
order_type_buttons.add(types.InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# Инлайн кнопки для оплаты
payment_buttons = types.InlineKeyboardMarkup()
payment_buttons.add(types.InlineKeyboardButton("Оплатить", callback_data='pay'))

# Состояния пользователя
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

# @dp.message_handler(text='Розы')
# async def roses(message: types.Message):
#     await message.reply_photo(
#         photo="https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg",
#         caption="Розы - 500 сомов за букет. Красивые и ароматные розы для любого случая.",
#         reply_markup=order_buttons
    # )
flower_data = {
    "Розы": [
        {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "price": 50000},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Розы - 550 сомов за букет.", "price": 55000},
        {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Розы - 600 сомов за букет.", "price": 60000},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s", "caption": "Розы - 650 сомов за букет.", "price": 65000},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s", "caption": "Розы - 700 сомов за букет.", "price": 70000},
    ],
    # Добавьте данные для других цветов здесь...
}




@dp.message_handler(text='Пионы')
async def peonies(message: types.Message):
    await message.reply_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s",
        caption="Пионы - 600 сомов за букет. Элегантные пионы, которые придают шарм.",
        reply_markup=order_buttons
    )

@dp.message_handler(text='Гипсофилы')
async def gypsophila(message: types.Message):
    await message.reply_photo(
        photo="https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478",
        caption="Гипсофила - 400 сомов за букет. Легкие и воздушные цветы для изысканного букета.",
        reply_markup=order_buttons
    )

@dp.message_handler(text='Ромашки')
async def daisies(message: types.Message):
    await message.reply_photo(
        photo="https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg",
        caption="Ромашки - 350 сомов за букет. Простые и милые ромашки, которые вызывают улыбку.",
        reply_markup=order_buttons
    )

@dp.message_handler(text='Лилии')
async def lilies(message: types.Message):
    await message.reply_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo-aoF9xAj_hai3F1omYPGTGiJCN3XfPhkWA&s",
        caption="Лилии - 700 сомов за букет. Великолепные лилии, которые привлекут внимание.",
        reply_markup=order_buttons
    )

@dp.message_handler(text='Гвоздики')
async def carnations(message: types.Message):
    await message.reply_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s",
        caption="Гвоздики - 450 сомов за букет. Прочные и красивые гвоздики для любого случая.",
        reply_markup=order_buttons
    )

@dp.callback_query_handler(lambda c: c.data == 'order')
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
            # # chat_id=user_id,
            # title="Оплата за букет",
            # description="Оплата за заказанный букет.",
            # payload="flower",  # Используйте уникальный идентификатор платежа
            # provider_token=pay_token,  # Токен вашего платёжного провайдера
            # start_parameter="test_bot",
            # currency="RUB",  # Введите вашу валюту
            # prices=[types.LabeledPrice(label="Букет", amount=50000)]  # Укажите цену (в копейках)
            await bot.send_invoice(
    chat_id=user_id,
    title="Оплата за букет",
    description="Оплата за заказанный букет.",
    payload="flower",  # Используйте уникальный идентификатор платежа
    provider_token=pay_token,  # Токен вашего платёжного провайдера
    start_parameter="test_bot",
    currency="RUB",  # Введите вашу валюту
    prices=[types.LabeledPrice(label="Букет", amount=user_states[user_id]['price'])]  # Укажите цену (в копейках)
)

        )

executor.start_polling(dp, skip_updates=True)






































































