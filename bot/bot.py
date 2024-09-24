import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from handlers import router


async def main():
    bot = Bot(token='7980634348:AAE-rVg8rystIG2_gnSYecVga8SUNo8Ao3Q')
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")