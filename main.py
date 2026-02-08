import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer('Коммит дев2.')


async def main() -> None:
    bot = Bot(token=TOKEN)
    
    await dp.start_polling(bot) 


if __name__ == '__main__':
    asyncio.run(main())
