# import smtplib
# from email.message import EmailMessage
# from config import smtp_sender,smtp_password

# def send_email(to_email,subject,message, image_path=None):
#     sender=smtp_sender
#     password=smtp_password

#     server=smtplib.SMTP("smtp.gmail.com",587) #  хостом и портом
#     server.starttls()

#     try:
#         server.login(sender,password)
#         msg =EmailMessage()
#         msg['Subject']=subject
#         msg['From']=sender
#         msg['To']=to_email
#         msg.set_content(message)
        
#         if image_path:
#             with open (image_path,'rb') as img:
#                 img_d = img.read()
#                 msg.add_attachment(img_d, maintype ='image',subtype='jpg',filename=image_path)
            
#             server.send_message(msg)
#         return "200 OK"
#     except Exception as error:
#         return f'Error {error}'
    
# print(send_email('telefonr499@gmail.com','Hello','Hello Islam',r'C:\Users\TM\Desktop\aiogram\3питон логотип.png'))









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

def create_confirmation_buttons():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Подтвердить", callback_data='confirm_order'),
        InlineKeyboardButton("Отменить", callback_data='cancel_order')
    )

order_type_buttons = InlineKeyboardMarkup()
order_type_buttons.add(InlineKeyboardButton("Доставка", callback_data='delivery'))
order_type_buttons.add(InlineKeyboardButton("Самовывоз", callback_data='self_pickup'))
order_type_buttons.add(InlineKeyboardButton("Назад", callback_data='back_to_flowers'))

payment_buttons = InlineKeyboardMarkup()
payment_buttons.add(InlineKeyboardButton("Оплатить", callback_data='pay'))


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
        {"photo": "https://flowercube.ru/wa-data/public/shop/products/20/07/720/images/1101/1101.750x0.jpg", "caption": "Ромашки - 400 сомов за букет.", "id": "daisies_2" , "price":400 },
        {"photo": "https://static.wixstatic.com/media/46e947_d83e9c774e1e4a78b5b1ed6b5dbd9a0e.jpg/v1/fill/w_480,h_480,al_c,lg_1,q_85/46e947_d83e9c774e1e4a78b5b1ed6b5dbd9a0e.jpg", "caption": "Ромашки - 450 сомов за букет.", "id": "daisies_3" , "price":450},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHm0aMWu8dybR__MYR1D7ShkFcc0YoVXh6ow&s", "caption": "Ромашки - 500 сомов за букет.", "id": "daisies_4" , "price":500},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQkm5CchL-URq1UjO2eq1kICaOXTyLG_G5Sg&s", "caption": "Ромашки - 550 сомов за букет.", "id": "daisies_5" , "price":550 }
    ],
    "Лилии": [
        {"photo": "https://florist-5d6c.kxcdn.com/upload/iblock/5a7/5a74f406a07264c65738fd5e626a862d.jpg", "caption": "Лилии - 600 сомов за букет.", "id": "lilies_1" , "price":600},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzGkK3A8KgnZ-7hn8hG3bxrGf6CD_r9kqYCA&s", "caption": "Лилии - 650 сомов за букет.", "id": "lilies_2" , "price":650},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1iD2uQYIcduzZyI5MZ7czZZJYNIS97v70VA&s", "caption": "Лилии - 700 сомов за букет.", "id": "lilies_3" , "price":700},
        {"photo": "https://florist-5d6c.kxcdn.com/upload/iblock/f34/f349a1f2a7e7265f68e567cc6cfda5bc.jpg", "caption": "Лилии - 750 сомов за букет.", "id": "lilies_4" , "price":750},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnOsFdXj3N5MJ5iDLfbD1kETNZtncSy8uHqA&s", "caption": "Лилии - 800 сомов за букет.", "id": "lilies_5" , "price":800 }
    ],
    "Гвоздики": [
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0UZ5N8iThXZlk8OR2pSC2jMHZLrl3fiE6Ew&s", "caption": "Гвоздики - 300 сомов за букет.", "id": "carnations_1" , "price":300},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGb2dmt4LwEieP4In2d-dMyDZ3QwN4vhq3IQ&s", "caption": "Гвоздики - 350 сомов за букет.", "id": "carnations_2" , "price":350},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1YEkIokb4iXc-7G2W-90qaOdRfwc2Bphqaw&s", "caption": "Гвоздики - 400 сомов за букет.", "id": "carnations_3" , "price":400},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUqS6koH47D2aUbHD92o1VbnFwZf0I5JxqCA&s", "caption": "Гвоздики - 450 сомов за букет.", "id": "carnations_4" , "price":450},
        {"photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy9cKp9e3Dyc2xlb87sciZPMgzVZ1m2ItV4Q&s", "caption": "Гвоздики - 500 сомов за букет.", "id": "carnations_5" , "price":500 }
    ],
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
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
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
                await bot.answer_callback_query(callback_query.id)
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
                
                
                await bot.send_message(user_id, "Пожалуйста, подтвердите ваш заказ.", reply_markup=create_confirmation_buttons())
                
               
                user_states[user_id]['status'] = 'awaiting_confirmation'
            except Exception as e:
                print(f"Ошибка при отправке инвойса: {e}")
                await bot.send_message(user_id, "Произошла ошибка при попытке оплаты. Попробуйте снова позже.")
        else:
            await bot.send_message(user_id, "Не удалось определить цену для выбранного букета.")
    else:
        await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и способ получения.")

@dp.callback_query_handler(lambda c: c.data == 'confirm_order')
async def confirm_order(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(user_id, "Вы подтвердили заказ. Спасибо за покупку!")
        
        del user_states[user_id]
    else:
        await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

@dp.callback_query_handler(lambda c: c.data == 'cancel_order')
async def cancel_order(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_confirmation':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(user_id, "Вы отменили заказ. Если у вас возникли вопросы, пожалуйста, свяжитесь с нами.")
      
        del user_states[user_id]
    else:
        await bot.send_message(user_id, "Пожалуйста, сначала выберите букет и оплатите его.")

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def handle_successful_payment(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_states and user_states[user_id].get('status') == 'awaiting_payment':
        await message.reply("Спасибо за ваш платеж! Ваш заказ принят.")
   

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)