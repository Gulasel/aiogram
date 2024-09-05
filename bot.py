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
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
#     )

# def create_confirmation_buttons():
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
#         InlineKeyboardButton("Отменить", callback_data='cancel_order')
#     )

# order_type_buttons = InlineKeyboardMarkup()
# order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
# order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
# order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# payment_buttons = InlineKeyboardMarkup()
# payment_buttons.add(InlineKeyboardButton("Оплатить", callback_data='pay'))


# user_states = {}

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

# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

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
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUTcGWRvqeG8LBMAYgI3NxqOt8xiGHoyPvbw&s", "caption": "Гипсофила - 550 сомов за букет.", "id": "gypsophila_4" , "price":550},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5" , "price":600}
#     ],
#     "Ромашки": [
#         {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет.", "id": "daisies_1" , "price":350},
#         {"photo": "https://flowercube.ru/wa-data/public/shop/products/20/07/720/images/1101/1101.750x0.jpg", "caption": "Ромашки - 400 сомов за букет.", "id": "daisies_2" , "price":400 },
#         {"photo": "https://static.wixstatic.com/media/46e947_d83e9c774e1e4a78b5b1ed6b5dbd9a0e.jpg/v1/fill/w_480,h_480,al_c,lg_1,q_85/46e947_d83e9c774e1e4a78b5b1ed6b5dbd9a0e.jpg", "caption": "Ромашки - 450 сомов за букет.", "id": "daisies_3" , "price":450},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHm0aMWu8dybR__MYR1D7ShkFcc0YoVXh6ow&s", "caption": "Ромашки - 500 сомов за букет.", "id": "daisies_4" , "price":500},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQkm5CchL-URq1UjO2eq1kICaOXTyLG_G5Sg&s", "caption": "Ромашки - 550 сомов за букет.", "id": "daisies_5" , "price":550 }
#     ],
#     "Лилии": [
#         {"photo": "https://florist-5d6c.kxcdn.com/upload/iblock/5a7/5a74f406a07264c65738fd5e626a862d.jpg", "caption": "Лилии - 600 сомов за букет.", "id": "lilies_1" , "price":600},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzGkK3A8KgnZ-7hn8hG3bxrGf6CD_r9kqYCA&s", "caption": "Лилии - 650 сомов за букет.", "id": "lilies_2" , "price":650},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1iD2uQYIcduzZyI5MZ7czZZJYNIS97v70VA&s", "caption": "Лилии - 700 сомов за букет.", "id": "lilies_3" , "price":700},
#         {"photo": "https://florist-5d6c.kxcdn.com/upload/iblock/f34/f349a1f2a7e7265f68e567cc6cfda5bc.jpg", "caption": "Лилии - 750 сомов за букет.", "id": "lilies_4" , "price":750},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnOsFdXj3N5MJ5iDLfbD1kETNZtncSy8uHqA&s", "caption": "Лилии - 800 сомов за букет.", "id": "lilies_5" , "price":800 }
#     ],
#     "Гвоздики": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0UZ5N8iThXZlk8OR2pSC2jMHZLrl3fiE6Ew&s", "caption": "Гвоздики - 300 сомов за букет.", "id": "carnations_1" , "price":300},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGb2dmt4LwEieP4In2d-dMyDZ3QwN4vhq3IQ&s", "caption": "Гвоздики - 350 сомов за букет.", "id": "carnations_2" , "price":350},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1YEkIokb4iXc-7G2W-90qaOdRfwc2Bphqaw&s", "caption": "Гвоздики - 400 сомов за букет.", "id": "carnations_3" , "price":400},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUqS6koH47D2aUbHD92o1VbnFwZf0I5JxqCA&s", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_4" , "price":450},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy9cKp9e3Dyc2xlb87sciZPMgzVZ1m2ItV4Q&s", "caption": "Гвоздики - 500 сомов за букет.", "id": "carnations_5" , "price":500 }
#     ],
# }

# @dp.message_handler(lambda message: message.text in flower_data.keys())
# async def handle_flower_choice(message: types.Message):
#     flower_type = message.text
#     flower_list = flower_data.get(flower_type)
    
#     if flower_list:
#         for flower in flower_list:
#             await bot.send_photo(message.chat.id, flower['photo'], caption=flower['caption'], reply_markup=create_order_buttons(flower['id']))
#     else:
#         await message.reply("Ошибка: не удалось найти данные о цветке.")

# @dp.callback_query_handler(lambda c: c.data.startswith('order_'))
# async def handle_order(callback_query: types.CallbackQuery):
#     flower_id = callback_query.data.split('_', 1)[1]
#     user_id = callback_query.from_user.id
    
    
#     user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)

# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def handle_order_type(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
#         flower_id = user_states[user_id].get('flower_id')
#         flower_name = None
#         price = None

#         for flower_category in flower_data.values():
#             for flower in flower_category:
#                 if flower['id'] == flower_id:
#                     flower_name = flower['caption']
#                     price = flower['price']
#                     break
#             if flower_name:
#                 break

#         if price is not None:
#             price_cents = price * 100  
#             try:
#                 await bot.answer_callback_query(callback_query.id)
#                 await bot.send_invoice(
#                     chat_id=user_id,
#                     title=flower_name,
#                     description="Оплата за заказанный букет.",
#                     payload=f"flower_{flower_id}",
#                     provider_token=pay_token,
#                     start_parameter="test_bot",
#                     currency="RUB",
#                     prices=[LabeledPrice(label=flower_name, amount=price_cents)]
#                 )
                
                
#                 await bot.send_message(user_id, "Пожалуйста, подтвердите ваш заказ.", reply_markup=create_confirmation_buttons())
                
               
#                 user_states[user_id]['status'] = 'awaiting_confirmation'
#             except Exception as e:
#                 print(f"Ошибка при отправке инвойса: {e}")
#                 await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
#         else:
#             await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и способ получения.")

# @dp.callback_query_handler(lambda c: c.data == 'confirm_order')
# async def confirm_order(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(user_id, "Вы подтвердили заказ. Спасибо за покупку!")
        
#         del user_states[user_id]
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

# @dp.callback_query_handler(lambda c: c.data == 'cancel_order')
# async def cancel_order(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(user_id, "Вы отменили заказ. Если у вас возникли вопросы, пожалуйста, свяжитесь с нами.")
      
#         del user_states[user_id]
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

# @dp.pre_checkout_query_handler()
# async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
# async def handle_successful_payment(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
#         await message.reply("Спасибо за ваш платеж! Ваш заказ принят.")
   

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




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
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
#     )

# def create_confirmation_buttons():
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
#         InlineKeyboardButton("Отменить", callback_data='cancel_order')
#     )

# order_type_buttons = InlineKeyboardMarkup()
# order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
# order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
# order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# user_states = {}

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

# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# @dp.message_handler(text='Назад')
# async def back_start(message: types.Message):
#     await start(message)

# flower_data = {
#     "Розы": [
#         {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1", "price": 500},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2", "price": 550},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.", "id": "roses_3", "price": 600},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4", "price": 650},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5", "price": 700},
#     ],
#     "Пионы": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv-OMqYHGzU2IgvxPrVR0Z-zvEM9tU9gQiDQ&s", "caption": "Пионы - 600 сомов за букет.", "id": "peonies_1", "price": 600},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj54ZnmbMI0MnchTsKWVeFhW6FRinXmF5mgQ&s", "caption": "Пионы - 650 сомов за букет.", "id": "peonies_2", "price": 650},
#         {"photo": "https://tsvetochnyybiznes.ru/upload/iblock/598/5980693b7113499296ae88bfae5bc259.jpg", "caption": "Пионы - 700 сомов за букет.", "id": "peonies_3", "price": 700},
#         {"photo": "https://static.insales-cdn.com/images/products/1/6619/187800027/IMG_8894-1_optimized.jpg", "caption": "Пионы - белые пионы 750 сомов за букет.", "id": "peonies_4", "price": 750},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRGR4eV0rkruNXhbZU5ZVDjQ4OOlQtOnhjiA&s", "caption": "Пионы - 800 сомов за букет.", "id": "peonies_5", "price": 800},
#     ],
#     "Гипсофилы": [
#         {"photo": "https://florcat.ru/upload/delight.webpconverter/upload/resize_cache/iblock/a8a/500_500_1/slo8zy7f1ayby4wn0wcogv5o9haj7kqy.jpg.webp?166844318639478", "caption": "Гипсофила - 400 сомов за букет.", "id": "gypsophila_1", "price": 400},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5yRmzkU4QC2pYQT2ygPkWewSPIeLo63x2Vw&s", "caption": "Гипсофила - 450 сомов за букет.", "id": "gypsophila_2", "price": 450},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPGHqxbtdExQma1uxxqTVCAugtLJxfuVhHUA&s", "caption": "Гипсофила - 500 сомов за букет.", "id": "gypsophila_3", "price": 500},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUTcGWRvqeG8LBMAYgI3NxqOt8xiGHoyPvbw&s", "caption": "Гипсофила - 550 сомов за букет.", "id": "gypsophila_4", "price": 550},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCQsQtkb200qU8TBD4_cpfOMlFusrmCqw7w&s", "caption": "Гипсофила - 600 сомов за букет.", "id": "gypsophila_5", "price": 600},
#     ],
#     "Ромашки": [
#         {"photo": "https://content2.flowwow-images.com/data/flowers/1000x1000/76/1688141595_94914276.jpg", "caption": "Ромашки - 350 сомов за букет.", "id": "daisies_1", "price": 350},
#         {"photo": "https://flowercube.ru/wa-data/public/shop/products/20/07/720/images/1101/1101.750x0.jpg", "caption": "Ромашки - 400 сомов за букет.", "id": "daisies_2", "price": 400},
#         {"photo": "https://flowersinaustralia.com/images/2017/08/flowers-and-daisies.jpg", "caption": "Ромашки - 450 сомов за букет.", "id": "daisies_3", "price": 450},
#         {"photo": "https://www.flower.com/flower-bouquets/images/large-daisies.jpg", "caption": "Ромашки - 500 сомов за букет.", "id": "daisies_4", "price": 500},
#         {"photo": "https://image.shutterstock.com/image-photo/beautiful-daisy-flowers-on-white-260nw-1110165406.jpg", "caption": "Ромашки - 550 сомов за букет.", "id": "daisies_5", "price": 550},
#     ],
#     "Лилии": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAXYMI8zexmDJDKQArEHKUoG8Wue8Jw6c2Lw&s", "caption": "Лилии - 650 сомов за букет.", "id": "lilies_1", "price": 650},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4n5FZj7Q5v6WOS0tf6eDCmB6jAsayF5l8vw&s", "caption": "Лилии - 700 сомов за букет.", "id": "lilies_2", "price": 700},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlzMUlq4fwv8gKNjfG2HE3lRTjThSkZZ5azw&s", "caption": "Лилии - 750 сомов за букет.", "id": "lilies_3", "price": 750},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_F7y6WSCZ3D9mDF8M2FYXwM0pHgRbIYl4NA&s", "caption": "Лилии - 800 сомов за букет.", "id": "lilies_4", "price": 800},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1QJ6GXB2bMxiHV3pA6P9jcA2-mErCz8XBPA&s", "caption": "Лилии - 850 сомов за букет.", "id": "lilies_5", "price": 850},
#     ],
#     "Гвоздики": [
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSppD4ShEZvXXpQ6QfFw5vZTydbC1S6h3vHEQ&s", "caption": "Гвоздики - 300 сомов за букет.", "id": "carnations_1", "price": 300},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO-3fL1oQ2P7GxDej1AXwSSJX0kvE3l1zwhQ&s", "caption": "Гвоздики - 350 сомов за букет.", "id": "carnations_2", "price": 350},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQovg3U7Hzz7iMKxgDhgzwchx0wZmtjFV0SMQ&s", "caption": "Гвоздики - 400 сомов за букет.", "id": "carnations_3", "price": 400},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNOLAXBOnsyv-X3JmC14l7jql98W3i4kkb5g&s", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_4", "price": 450},
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZTQfSl2sXKhvsugkAYRC67sOZbVKNmM8hwA&s", "caption": "Гвоздики - 500 сомов за букет.", "id": "carnations_5", "price": 500},
#     ],
# }

# @dp.message_handler(lambda message: message.text in flower_data)
# async def send_flower_options(message: types.Message):
#     flower_type = message.text
#     flowers = flower_data[flower_type]
#     for flower in flowers:
#         photo = flower["photo"]
#         caption = flower["caption"]
#         flower_id = flower["id"]
#         await message.answer_photo(photo=photo, caption=caption, reply_markup=create_order_buttons(flower_id))

# @dp.callback_query_handler(lambda c: c.data.startswith('order_'))
# async def process_order(callback_query: types.CallbackQuery):
#     flower_id = callback_query.data.split('_')[1]
#     user_states[callback_query.from_user.id] = {"flower_id": flower_id, "address": None, "phone": None}
#     await callback_query.message.answer("Выберите тип заказа", reply_markup=order_type_buttons)

# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def handle_order_type(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if callback_query.data == 'self_pickup':
#         user_states[user_id]["address"] = "Самовывоз"
#         await callback_query.message.answer("Вы выбрали самовывоз. Пожалуйста, подтвердите свой заказ.", reply_markup=create_confirmation_buttons())
#     elif callback_query.data == 'delivery':
#         await callback_query.message.answer("Пожалуйста, отправьте ваш номер телефона.", reply_markup=types.ReplyKeyboardRemove())
#         await bot.send_message(callback_query.from_user.id, "После ввода номера телефона, пожалуйста, отправьте ваш адрес.")
#         user_states[user_id]["address"] = "Ожидание номера телефона"

# @dp.message_handler(lambda message: message.contact and user_states.get(message.from_user.id) and user_states[message.from_user.id]["address"] == "Ожидание номера телефона")
# async def handle_phone_number(message: types.Message):
#     user_id = message.from_user.id
#     user_states[user_id]["phone"] = message.contact.phone_number
#     await message.answer("Спасибо! Пожалуйста, отправьте ваш адрес.")
#     user_states[user_id]["address"] = "Ожидание адреса"

# @dp.message_handler(lambda message: user_states.get(message.from_user.id) and user_states[message.from_user.id]["address"] == "Ожидание адреса")
# async def handle_address(message: types.Message):
#     user_id = message.from_user.id
#     user_states[user_id]["address"] = message.text
#     await message.answer("Пожалуйста, подтвердите свой заказ.", reply_markup=create_confirmation_buttons())

# @dp.callback_query_handler(lambda c: c.data in ['confirm_order', 'cancel_order'])
# async def handle_confirmation(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if callback_query.data == 'confirm_order':
#         state = user_states.get(user_id)
#         if state:
#             flower_id = state.get("flower_id")
#             phone = state.get("phone", "Не предоставлен")
#             address = state.get("address", "Не предоставлен")
#             await callback_query.message.answer(f"Ваш заказ подтвержден!\n\nЦветок: {flower_id}\nТелефон: {phone}\nАдрес: {address}")
#             user_states.pop(user_id, None)  # Очистить состояние пользователя
#         else:
#             await callback_query.message.answer("Ошибка подтверждения заказа.")
#     elif callback_query.data == 'cancel_order':
#         user_states.pop(user_id, None)  # Очистить состояние пользователя
#         await callback_query.message.answer("Ваш заказ отменен.")

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)







# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
# from config import token, pay_token
# from logging import basicConfig, INFO

# # Создание объекта бота и диспетчера
# bot = Bot(token=token)
# dp = Dispatcher(bot)

# # Настройка логирования
# basicConfig(level=INFO)

# # Кнопки для главного меню
# start_buttons = [
#     types.KeyboardButton('Цветы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес')
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# # Кнопки для выбора типа цветов
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

# # Создание кнопок для заказа цветка
# def create_order_buttons(flower_id):
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
#     )

# # Создание кнопок для подтверждения или отмены заказа
# def create_confirmation_buttons():
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
#         InlineKeyboardButton("Отменить", callback_data='cancel_order')
#     )

# # Кнопки для выбора типа получения заказа
# order_type_buttons = InlineKeyboardMarkup()
# order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
# order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
# order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# # Кнопки для оплаты
# payment_buttons = InlineKeyboardMarkup()
# payment_buttons.add(InlineKeyboardButton("Оплатить", callback_data='pay'))

# # Хранение состояний пользователей
# user_states = {}

# # Обработка команды /start
# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)

# # Обработка кнопки "Контакты"
# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer('Вот наши контакты: ')
#     await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
#     await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")

# # Обработка кнопки "Адрес"
# @dp.message_handler(text='Адрес')
# async def send_address(message: types.Message):
#     await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
#     await message.reply_location(40.519225, 72.812685)

# # Обработка кнопки "Цветы"
# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)

# # Обработка кнопки "Назад"
# @dp.message_handler(text='Назад')
# async def back_start(message: types.Message):
#     await start(message)

# # Данные о цветах
# flower_data = {
#     "Розы": [
#         {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1" , "price":500 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2" , "price":550 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.","id": "roses_3" , "price":600 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4" , "price":650 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5" , "price":700 },
#     ],
#     # Данные для других видов цветов...
# }

# # Обработка выбора типа цветов
# @dp.message_handler(lambda message: message.text in flower_data.keys())
# async def handle_flower_choice(message: types.Message):
#     flower_type = message.text
#     flower_list = flower_data.get(flower_type)
    
#     if flower_list:
#         for flower in flower_list:
#             await bot.send_photo(message.chat.id, flower['photo'], caption=flower['caption'], reply_markup=create_order_buttons(flower['id']))
#     else:
#         await message.reply("Ошибка: не удалось найти данные о цветке.")

# # Обработка нажатия на кнопку "Заказать"
# @dp.callback_query_handler(lambda c: c.data.startswith('order_'))
# async def handle_order(callback_query: types.CallbackQuery):
#     flower_id = callback_query.data.split('_', 1)[1]
#     user_id = callback_query.from_user.id
    
#     # Сохранение состояния пользователя
#     user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)

# # Обработка выбора способа получения заказа
# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def handle_order_type(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
#        resize_keyboard=True,
#         one_time_keyboard=True
#     ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
#         flower_id = user_states[user_id].get('flower_id')
#         flower_name = None
#         price = None

#         for flower_category in flower_data.values():
#             for flower in flower_category:
#                 if flower['id'] == flower_id:
#                     flower_name = flower['caption']
#                     price = flower['price']
#                     break
#             if flower_name:
#                 break

#         if price is not None:
#             price_cents = price * 100  
#             try:
#                 await bot.answer_callback_query(callback_query.id)
#                 await bot.send_invoice(
#                     chat_id=user_id,
#                     title=flower_name,
#                     description="Оплата за заказанный букет.",
#                     payload=f"flower_{flower_id}",
#                     provider_token=pay_token,
#                     start_parameter="test_bot",
#                     currency="RUB",
#                     prices=[LabeledPrice(label=flower_name, amount=price_cents)]
#                 )
                
#                 await bot.send_message(user_id, "Пожалуйста, подтвердите ваш заказ.", reply_markup=create_confirmation_buttons())
                
#                 user_states[user_id]['status'] = 'awaiting_confirmation'
#             except Exception as e:
#                 print(f"Ошибка при отправке инвойса: {e}")
#                 await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
#         else:
#             await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и способ получения.")

# Обработка подтверждения заказа
# @dp.callback_query_handler(lambda c: c.data == 'confirm_order')
# async def confirm_order(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(user_id, "Вы подтвердили заказ. Спасибо за покупку!")
        
#         del user_states[user_id]
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

# Обработка отмены заказа
# @dp.callback_query_handler(lambda c: c.data == 'cancel_order')
# async def cancel_order(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(user_id, "Вы отменили заказ. Если у вас возникли вопросы, пожалуйста, свяжитесь с нами.")
        
#         del user_states[user_id]
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

# Обработка успешной оплаты


# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
# from config import token, pay_token
# from logging import basicConfig, INFO

# # Создание объекта бота и диспетчера
# bot = Bot(token=token)  # Инициализируем бота с токеном из конфигурации
# dp = Dispatcher(bot)  # Создаем диспетчер для обработки входящих сообщений

# # Настройка логирования
# basicConfig(level=INFO)  # Настройка уровня логирования для отображения информационных сообщений

# # Кнопки для главного меню
# start_buttons = [
#     types.KeyboardButton('Цветы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес')
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)  # Создание клавиатуры с кнопками главного меню

# # Кнопки для выбора типа цветов
# flower_buttons = [
#     types.KeyboardButton("Розы"),
#     types.KeyboardButton("Пионы"),
#     types.KeyboardButton("Гипсофилы"),
#     types.KeyboardButton("Ромашки"),
#     types.KeyboardButton("Лилии"),
#     types.KeyboardButton("Гвоздики"),
#     types.KeyboardButton("Назад")
# ]
# flowers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*flower_buttons)  # Клавиатура для выбора типа цветов

# # Создание кнопок для заказа цветка
# def create_order_buttons(flower_id):
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Заказать", callback_data=f'order_{flower_id}')
#     )

# # Создание кнопок для подтверждения или отмены заказа
# def create_confirmation_buttons():
#     return InlineKeyboardMarkup().add(
#         InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
#         InlineKeyboardButton("Отменить", callback_data='cancel_order')
#     )

# # Кнопки для выбора типа получения заказа
# order_type_buttons = InlineKeyboardMarkup()
# order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
# order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
# order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

# # Кнопки для оплаты
# payment_buttons = InlineKeyboardMarkup()
# payment_buttons.add(InlineKeyboardButton("Оплатить", callback_data='pay'))

# # Хранение состояний пользователей
# user_states = {}  # Словарь для хранения состояния пользователя

# # Обработка команды /start
# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Здравствуйте \nРады приветствовать вас в нашем магазине. У нас вы можете заказать букет!', reply_markup=start_keyboard)
#     # Отправляем приветственное сообщение и показываем главную клавиатуру

# # Обработка кнопки "Контакты"
# @dp.message_handler(text='Контакты')
# async def contact(message: types.Message):
#     await message.answer('Вот наши контакты: ')
#     await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
#     await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")
#     # Отправляем контактные данные

# # Обработка кнопки "Адрес"
# @dp.message_handler(text='Адрес')
# async def send_address(message: types.Message):
#     await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
#     await message.reply_location(40.519225, 72.812685)
#     # Отправляем адрес и географическое положение

# # Обработка кнопки "Цветы"
# @dp.message_handler(text='Цветы')
# async def send_flowers(message: types.Message):
#     await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)
#     # Отправляем сообщение с предложением выбрать вид цветов и показываем клавиатуру с вариантами

# # Обработка кнопки "Назад"
# @dp.message_handler(text='Назад')
# async def back_start(message: types.Message):
#     await start(message)
#     # Возвращаемся в главное меню

# # Данные о цветах
# flower_data = {
#     "Розы": [
#         {"photo": "https://zarum.ru/uploads/posts/2023-08/1692524790_4dd0c455-c322-423c-ba63-683dcc61a893.jpeg", "caption": "Розы - 500 сомов за букет.", "id": "roses_1" , "price":500 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLX5QmaubQDZ0SsckEsYknZrJaamTC9v5Bg&s", "caption": "Розы - 550 сомов за букет.", "id": "roses_2" , "price":550 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UqKwHREasy-8MS3ejU9J6RvjBDDF3TU4bA&s", "caption": "Розы - 600 сомов за букет.","id": "roses_3" , "price":600 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT67f5Q-1LCCDsqAk6ls_i3YqZoXYP8ns2Kyw&s", "caption": "Розы - 650 сомов за букет.", "id": "roses_4" , "price":650 },
#         {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzHMpme3SMjTVQTKPYD6v6-GnD39g9hZbhiQ&s", "caption": "Розы - 700 сомов за букет.", "id": "roses_5" , "price":700 },
#     ],
#     # Данные для других видов цветов будут добавлены аналогичным образом
# }

# # Обработка выбора типа цветов
# @dp.message_handler(lambda message: message.text in flower_data.keys())
# async def handle_flower_choice(message: types.Message):
#     flower_type = message.text  # Определяем тип цветов, выбранный пользователем
#     flower_list = flower_data.get(flower_type)  # Получаем данные для выбранного типа цветов
    
#     if flower_list:
#         for flower in flower_list:
#             await bot.send_photo(message.chat.id, flower['photo'], caption=flower['caption'], reply_markup=create_order_buttons(flower['id']))
#             # Отправляем фото и описание каждого букета с кнопкой для заказа
#     else:
#         await message.reply("Ошибка: не удалось найти данные о цветке.")
#         # Сообщаем об ошибке, если данные не найдены

# # Обработка нажатия на кнопку "Заказать"
# @dp.callback_query_handler(lambda c: c.data.startswith('order_'))
# async def handle_order(callback_query: types.CallbackQuery):
#     flower_id = callback_query.data.split('_', 1)[1]  # Извлекаем ID выбранного букета
#     user_id = callback_query.from_user.id  # Получаем ID пользователя
    
#     # Сохранение состояния пользователя
#     user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
#     await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
#     await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)
#     # Просим пользователя выбрать способ получения заказа

# # Обработка выбора способа получения заказа
# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def handle_order_type(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id  # Получаем ID пользователя
    
#     await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
#     await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
#        resize_keyboard=True,
#         one_time_keyboard=True
#     ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
#     # Просим пользователя отправить контактные данные
    
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
#         flower_id = user_states[user_id].get('flower_id')  # Получаем ID выбранного букета
#         flower_name = None
#         price = None

#         # Находим название и цену букета по его ID
#         for flower_category in flower_data.values():
#             for flower in flower_category:
#                 if flower['id'] == flower_id:
#                     flower_name = flower['caption']
#                     price = flower['price']
#                     break
#             if flower_name:
#                 break

#         if price is not None:
#             price_cents = price * 100  # Переводим цену в копейки
#             try:
#                 await bot.send_invoice(
#                     chat_id=user_id,
#                     title=flower_name,
#                     description="Оплата за заказанный букет.",
#                     payload=f"flower_{flower_id}",
#                     provider_token=pay_token,
#                     start_parameter="test_bot",
#                     currency="RUB",
#                     prices=[LabeledPrice(label=flower_name, amount=price_cents)]
#                 )
#                 # Отправляем инвойс для оплаты
#                 await bot.send_message(user_id, "Пожалуйста, подтвердите ваш заказ.", reply_markup=create_confirmation_buttons())
#                 # Просим пользователя подтвердить заказ
                
#                 user_states[user_id]['status'] = 'awaiting_confirmation'
#             except Exception as e:
#                 print(f"Ошибка при отправке инвойса: {e}")
#                 await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
#                 # Обрабатываем ошибку, если что-то пошло не так
#         else:
#             await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
#             # Сообщаем об ошибке, если не удалось определить цену
#     else:
#         await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и способ получения.")
#         # Сообщаем об ошибке, если пользователь не выбрал букет или способ получения

# @dp.pre_checkout_query_handler(lambda query: True)
# async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# # Обработка успешной оплаты
# @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
# async def handle_successful_payment(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
#         await message.answer("Оплата прошла успешно. Спасибо за ваш заказ!")
#         del user_states[user_id]
#     else:
#         await message.answer("Не удалось подтвердить ваш заказ. Пожалуйста, попробуйте снова.")

# # Запуск бота
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
    # Отправляем приветственное сообщение и показываем главную клавиатуру

# Обработка кнопки "Контакты"
@dp.message_handler(text='Контакты')
async def contact(message: types.Message):
    await message.answer('Вот наши контакты: ')
    await message.answer_contact("+996500232632", "Gulasel", "Kamalova")
    await message.answer_contact("+996990130081", "Eliza", "Erkinbekova")
    # Отправляем контактные данные

# Обработка кнопки "Адрес"
@dp.message_handler(text='Адрес')
async def send_address(message: types.Message):
    await message.reply("Наш адрес: Город Ош, 275 А.Шакирова ул ")
    await message.reply_location(40.519225, 72.812685)
    # Отправляем адрес и географическое положение

# Обработка кнопки "Цветы"
@dp.message_handler(text='Цветы')
async def send_flowers(message: types.Message):
    await message.answer("Выберите вид цветов", reply_markup=flowers_keyboard)
    # Отправляем сообщение с предложением выбрать вид цветов и показываем клавиатуру с вариантами

# Обработка кнопки "Назад"
@dp.message_handler(text='Назад')
async def back_start(message: types.Message):
    await start(message)
    # Возвращаемся в главное меню

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
            # Отправляем фото и описание каждого букета с кнопкой для заказа
    else:
        await message.reply("Ошибка: не удалось найти данные о цветке.")
        # Сообщаем об ошибке, если данные не найдены

# Обработка нажатия на кнопку "Заказать"
@dp.callback_query_handler(lambda c: c.data.startswith('order_'))
async def handle_order(callback_query: types.CallbackQuery):
    flower_id = callback_query.data.split('_', 1)[1]  # Извлекаем ID выбранного букета
    user_id = callback_query.from_user.id  # Получаем ID пользователя
    
    # Сохранение состояния пользователя
    user_states[user_id] = {'flower_id': flower_id, 'status': 'awaiting_payment'}
    
    await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
    await bot.send_message(user_id, "Вы выбрали заказ. Выберите способ получения.", reply_markup=order_type_buttons)
    # Просим пользователя выбрать способ получения заказа

# # Обработка выбора способа получения заказа
# @dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
# async def handle_order_type(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id  # Получаем ID пользователя
    
#     await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
#     await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
#        resize_keyboard=True,
#         one_time_keyboard=True
#     ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
#     # Просим пользователя отправить контактные данные

@dp.callback_query_handler(lambda c: c.data in ['delivery', 'self_pickup'])
async def handle_order_type(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    order_type = callback_query.data

    # Сохраняем тип заказа
    user_states[user_id]['order_type'] = order_type

    await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback запрос
    
    if order_type == 'delivery':
        # Запрашиваем номер телефона для доставки
        user_states[user_id]['status'] = 'awaiting_phone'
        await bot.send_message(user_id, "Вы выбрали доставку. Пожалуйста, укажите ваш номер телефона.", reply_markup=types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            one_time_keyboard=True
        ).add(types.KeyboardButton("Отправить контакт", request_contact=True)))
    elif order_type == 'self_pickup':
        # Немедленно отправляем инвойс для самовывоза
        await process_self_pickup(callback_query)
    @dp.message_handler(content_types=types.ContentType.CONTACT)
async def handle_phone(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_phone':
        user_states[user_id]['phone'] = message.contact.phone_number
        user_states[user_id]['status'] = 'awaiting_address'
        await message.reply("Теперь укажите адрес доставки.")



    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
        flower_id = user_states[user_id].get('flower_id')  # Получаем ID выбранного букета
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
                # Удаляем строку с кнопками подтверждения
                user_states[user_id]['status'] = 'awaiting_confirmation'
            except Exception as e:
                print(f"Ошибка при отправке инвойса: {e}")
                await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
                # Обрабатываем ошибку, если что-то пошло не так
        else:
            await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
            # Сообщаем об ошибке, если не удалось определить цену
    else:
        await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и способ получения.")
        # Сообщаем об ошибке, если пользователь не выбрал букет или способ получения

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
