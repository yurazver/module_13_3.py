
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor

API_TOKEN = '********8'


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    welcome_text = "Привет! Я ваш бот. Чем могу помочь?"
    await message.answer(welcome_text)

@dp.message_handler()
async def all_messages(message: types.Message):
    response_text = f"Вы написали: {message.text}"
    await message.answer(response_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)