import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

bot = Bot(token='7980634348:AAE-rVg8rystIG2_gnSYecVga8SUNo8Ao3Q')
dp = Dispatcher(bot=bot)

@dp.message()
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Приветствую")


@dp.message()
async def self_echo(msg: types.Message) -> None:
    print(msg)
    await msg.answer(msg.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())