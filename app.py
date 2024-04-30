import logging
from aiogram import Bot, Dispatcher, types
from config import Config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

async def start_bot():
    await dp.start_polling()

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
