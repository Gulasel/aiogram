import random

from aiogram import Bot, Dispatcher, types, executor


token='7011991566:AAFJreIBegl5nvCbIN8HaVtENBi56zau9Sk'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет, Я загадал число от 1 до 3. Попробуйте угадать! ")
   
    
@dp.message_handler(lambda message: message.text.isdigit() and int(message.text) in [1, 2, 3])

async def guess_number(message: types.Message):
    user_guess = int(message.text)
    secret_number = random.randint(1, 3)
    
    if user_guess == secret_number:
        await message.reply(f"Правильно! Вы отгадали число {secret_number}!")
       
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.reply(f"Вы не угадали. Я загадал число {secret_number}.")
        
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')
        
        
executor.start_polling(dp)



















