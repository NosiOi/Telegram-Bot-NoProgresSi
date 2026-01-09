import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8383656149:AAHU6a8xUof8MTxUmj238C3rX-2shKaaDI0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Доброго здоров'ячка! Бот працює.")

if __name__ == "__main__":
    asyncio.run(executor.start_polling(dp, skip_updates=True))
