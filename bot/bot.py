import asyncio
import datetime as dt
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.filters import CommandStart, Command
from handlers import router
from handlers import bot
# import logging
# from decouple import config


async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await set_commands(bot)
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