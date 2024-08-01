# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import Message
# from aiogram.dispatcher.storage import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import BotCommand

# from config import token
# from database import Database
# import logging

# bot = Bot(token=token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# db = Database('sql.db')
# db.create_table()
# logging.basicConfig(level=logging.INFO)

# class Form(StatesGroup):
#     username = State() 

# @dp.message_handler(commands='start')
# async def start(message:Message):
#     await Form.username.set()
#     await message.reply("Привет! Как тебя зовут ?")
    
# @dp.message_handler(state=Form.username)
# async def process_username(message:Message, state: FSMContext):
#     username = message.text
#     db.add_user(message.from_user.id, username)
#     await state.finish()
#     await message.reply(f'Приятно познакомиться, {username}')
    
# @dp.message_handler(commands='me')
# async def get_me(message:Message):
#     user = db.get_user(message.from_user.id)
#     if user:
#         await message.reply(f'Ты зарегистрирован как {user[2]}')
#     else:
#         await message.reply("Ты еще не зарегистрирован")
    
# async def on_startup(dp):
#     await bot.set_my_commands([
#         BotCommand(command='/start', description='Start bot'),
#         BotCommand(command='/me', description='Info me')
#     ])
#     logging.info("Настройки базы данных")
#     db.create_table()
#     logging.info("База загружена")
    
# executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


    
# @dp.message_handler(text="Назад")
# async def back_start(message:types.Message):
#     await start(message)

# @dp.message_handler(commands='start')
# async def start(message:Message):
#     await Form.username.set()
#     await message.reply("Сколько тебе лет ?")
    
    
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import Message
# from aiogram.dispatcher.storage import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import BotCommand

# from config import token
# from database import Database
# import logging

# bot = Bot(token=token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# db = Database('sql.db')
# db.create_table()
# logging.basicConfig(level=logging.INFO)

# class Form(StatesGroup):
#     username = State()
#     age = State()

# @dp.message_handler(commands='start')
# async def start(message: Message):
#     await Form.username.set()
#     await message.reply("Привет! Как тебя зовут?")

# @dp.message_handler(state=Form.username)
# async def process_username(message: Message, state: FSMContext):
#     username = message.text
#     db.add_user(message.from_user.id, username)
#     await state.finish()
#     await message.reply(f'Приятно познакомиться, {username}')
    
# @dp.message_handler(commands='age')
# async def start(message:Message):
#     await Form.username.set()
#     await message.reply("Сколько тебе лет ?")

# @dp.message_handler(state=Form.age)
# async def process_age(message: Message, state: FSMContext):
#     try:
#         age = int(message.text)
#         db.update_user_age(message.from_user.id, age)
#         await state.finish()
#         await message.reply(f'Возраст сохранен: {age}')
#     except ValueError:
#         await message.reply("Пожалуйста, введите возраст числом.")

# @dp.message_handler(commands='me')
# async def get_me(message: Message):
#     user = db.get_user(message.from_user.id)
#     if user:
#         reply_markup = types.InlineKeyboardMarkup()
#         reply_markup.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
#         await message.reply(f'Ты зарегистрирован как {user[2]}', reply_markup=reply_markup)
#     else: 
#         await message.reply("Ты еще не зарегистрирован")

# @dp.callback_query_handler(lambda query: query.data == 'back', state='*')
# async def back_to_username(query: types.CallbackQuery):
#     await Form.username.set()
#     await query.message.edit_text("Привет! Как тебя зовут?")
    
        
# @dp.message_handler(text="Назад")
# async def back_start(message:types.Message):
#     await start(message)

# async def on_startup(dp):
#     await bot.set_my_commands([
#         BotCommand(command='/start', description='Start bot'),
#         BotCommand(command='/me', description='Info me')
#     ])
#     logging.info("Настройки базы данных")
#     db.create_table()
#     logging.info("База загружена")

# executor.start_polling(dp, on_startup=on_startup, skip_updates=True)




# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import Message
# from aiogram.dispatcher.storage import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import BotCommand

# from config import token
# from database import Database
# import logging

# bot = Bot(token=token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# db = Database('sql.db')
# db.create_table()
# logging.basicConfig(level=logging.INFO)

# class Form(StatesGroup):
#     username = State()
#     age = State()

# @dp.message_handler(commands='start')
# async def start(message: Message):
#     await Form.username.set()
#     await message.reply("Привет! Как тебя зовут?")

# @dp.message_handler(state=Form.username)
# async def process_username(message: Message, state: FSMContext):
#     username = message.text
#     db.add_user(message.from_user.id, username)
#     await Form.age.set()
#     await message.reply(f'Сколько тебе лет')

# @dp.message_handler(state=Form.age)
# async def process_age(message: Message, state: FSMContext):
#     try:
#         age = int(message.text)
#         db.update_user_age(message.from_user.id, age)
#         await state.finish()
#         await message.reply(f'Возраст сохранен: {age}')
#     except ValueError:
#         await message.reply("Пожалуйста, введите возраст числом.")

# @dp.message_handler(commands='me')
# async def get_me(message: Message):
#     user = db.get_user(message.from_user.id)
#     if user:
#         reply_markup = types.InlineKeyboardMarkup()
#         reply_markup.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
#         await message.reply(f'Ты зарегистрирован как {user[2]}', reply_markup=reply_markup)
#     else:
#         await message.reply("Ты еще не зарегистрирован")

# @dp.callback_query_handler(lambda query: query.data == 'back', state='*')
# async def back_to_username(query: types.CallbackQuery):
#     await Form.username.set()
#     await query.message.edit_text("Привет! Как тебя зовут?")

# async def on_startup(dp):
#     await bot.set_my_commands([
#         BotCommand(command='/start', description='Start bot'),
#         BotCommand(command='/me', description='Info me')
#     ])
#     logging.info("Настройки базы данных")
#     db.create_table()
#     logging.info("База загружена")

# executor.start_polling(dp, on_startup=on_startup, skip_updates=True)



from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import token
from database import Database
import logging

# Инициализация бота, хранилища и диспетчера
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('sql.db')
db.create_table()
logging.basicConfig(level=logging.INFO)

# Класс для определения состояний
class Form(StatesGroup):
    username = State()
    age = State()

# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(message: Message):
    await Form.username.set()
    await message.reply("Привет! Как тебя зовут?")

# Обработчик ввода имени пользователя
@dp.message_handler(state=Form.username)
async def process_username(message: Message, state: FSMContext):
    username = message.text
    db.add_user(message.from_user.id, username)
    await Form.age.set()
    await message.reply("Сколько тебе лет?")

# Обработчик ввода возраста пользователя
@dp.message_handler(state=Form.age)
async def process_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        db.update_user_age(message.from_user.id, age)
        await state.finish()
        await message.reply(f'Возраст сохранен: {age}')
    except ValueError:
        await message.reply("Пожалуйста, введите возраст числом.")

# Обработчик команды /me для получения информации о пользователе
@dp.message_handler(commands='me')
async def get_me(message: Message):
    user = db.get_user(message.from_user.id)
    if user:
        # Создание кнопки "Назад"
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
        await message.reply(f'Ты зарегистрирован как {user[1]}', reply_markup=reply_markup)
    else:
        await message.reply("Ты еще не зарегистрирован")

# Обработчик нажатия кнопки "Назад"
@dp.callback_query_handler(lambda query: query.data == 'back', state='*')
async def back_to_username(query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == 'Form.age':
        await Form.username.set()
        await query.message.edit_text("Привет! Как тебя зовут?")
    else:
        await query.message.answer("Невозможно выполнить операцию, вернитесь в начало.")

# Задание команд бота при старте
async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command='/start', description='Начать диалог'),
        BotCommand(command='/me', description='Информация о пользователе')
    ])
    logging.info("Настройка базы данных")
    db.create_table()
    logging.info("База данных готова к работе")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=True)
