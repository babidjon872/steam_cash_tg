import asyncio
import datetime as dt
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from handlers import router
# import logging


async def main():
    bot = Bot(token='7980634348:AAE-rVg8rystIG2_gnSYecVga8SUNo8Ao3Q')
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logger = logging.getLogger(__name__)
    # logging.basicConfig(filename="./logs/startstop.log")
    # logger.warning(f"Bot started work at:{dt.datetime.now().strftime("%d.%m.%Y|%H:%M")}")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # logger.warning(f"Bot ended work at:{dt.datetime.now().strftime("%d.%m.%Y|%H:%M")}")
        print("Бот выключен")