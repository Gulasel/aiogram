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
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
    )

order_type_buttons = InlineKeyboardMarkup()
order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))


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
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjgL7lnpaqL56gWkHg0-RqZcUzRzAJHwr1gQ&s", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5" , "price":600}
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


@dp.message_handler(lambda message: message.text in flower_data.keys())
async def handle_flower_choice(message: types.Message):
    flower_type = message.text  
    flower_list = flower_data.get(flower_type)  
    
    if flower_list:
        for flower in flower_list:
            await bot.send_photo(message.chat.id, flower['photo'], caption=flower['caption'], reply_markup=create_order_buttons(flower['id']))
    else:
        await message.reply("Ошибка: не удалось найти данные о цветке.")


@dp.callback_query_handler(lambda c: c.data.startswith('order_'))
async def handle_order(callback_query: types.CallbackQuery):
    flower_id = callback_query.data.split('_', 1)[1]  
    user_id = callback_query.from_user.id  
    
    
    user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
    await bot.answer_callback_query(callback_query.id)  
    await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)


@dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
async def handle_order_type(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    order_type = callback_query.data
    

    if user_id in user_states:
        user_states[user_id]['order_type'] = order_type
    
    await bot.answer_callback_query(callback_query.id)  
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=callback_query.message.message_id, reply_markup=None)
    
    if order_type == 'delivery':
    
        await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона и адрес.",
                               reply_markup=types.ReplyKeyboardMarkup(
                                   resize_keyboard=True,
                                   one_time_keyboard=True
                               ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
        user_states[user_id]['status'] = 'awaiting_contact'
    elif order_type == 'self_pickup':
     
        await bot.send_message(user_id, "Вы выбрали самовывоз. Приходите в наш магазин по адресу: Город Ош, 275 А.Шакирова ул")
        del user_states[user_id]  


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def handle_contact(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_contact':
        contact = message.contact
        phone_number = contact.phone_number
        
      
        await bot.send_message(user_id, "Пожалуйста, укажите ваш адрес.")
        user_states[user_id]['status'] = 'awaiting_address'
        user_states[user_id]['contact'] = phone_number


@dp.message_handler(lambda message: user_states.get(message.from_user.id, {}).get('status') == 'awaiting_address')
async def handle_address(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_address':
        address = message.text
        
        
        flower_id = user_states[user_id].get('flower_id')
        flower_name = None
        price = None

        for flower_category in flower_data.values():
            for flower in flower_category:
                if flower['id'] == flower_id:
                    flower_name = flower['caption']
                    price = flower['price']
                    break
            if flower_name:
                break

        if price is not None:
            price_cents = price * 100  
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


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
        await message.answer("Оплата прошла успешно. Спасибо за ваш заказ!")
        del user_states[user_id]
    else:
        await message.answer("Не удалось подтвердить ваш заказ. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


