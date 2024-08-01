from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 

bot = Bot(token='7309642253:AAEZPlt0T4RxZ4P93QsGaSxR9e3oEJNVmQY')
dp = Dispatcher(bot)

notes=[]
@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer("Привет! Используй /add, чтобы добавить заметку, и /notes, чтобы просмотреть все заметки. Для помощи отправь /help.")

@dp.message_handler(commands='add')
async def add(message:types.Message):
    await message.answer(" Напишите заметку, которую хотите добавить.")

async def add_note(message: types.Message, state: FSMContext):
    notes.append(message.text)
    await state.finish()  
    await message.answer("Заметка добавлена!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
executor.start_polling(dp)