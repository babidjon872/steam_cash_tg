import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Register(StatesGroup):
    name = State()

router = Router()


@router.message(Command('register'))
async def register(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(Register.name)
    await msg.answer('Введите имя аккаунта Steam', reply_markup=kb.get_name)


@router.message(Register.name)
async def register_name(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(name=msg.text)

@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Приветствую", reply_markup=kb.main)
    await msg.answer("Что вас интересует?")


@router.message(F.text == 'Помощь')
async def cmd_help(msg: types.Message) -> None:
    await msg.answer('С чем возникла проблема?', reply_markup=kb.pomosh)


@router.message(F.text == 'Пополнение')
async def cmd_replenishment(msg: types.Message) -> None:
    await msg.answer('Выберите сумму пополнения', reply_markup=kb.replenishment)


@router.message(F.text == 'О нас')
async def cmd_about(msg: types.Message) -> None:
    await msg.answer('Пока что данный раздел пуст')


@router.callback_query(F.data == '300 руб')
async def cmd_300(callback: CallbackQuery) -> None:
    await callback.answer('Вы выбрали 300 руб')
    await callback.message.answer('Выберите способ пополнения', reply_markup=kb.replenishment300)


@router.callback_query(F.data == '600 руб')
async def cmd_600(callback: CallbackQuery) -> None:
    await callback.answer('Вы выбрали 600 руб')
    await callback.message.answer('Выберите способ пополнения', reply_markup=kb.replenishment600)


@router.callback_query(F.data == '1200 руб')
async def cmd_1200(callback: CallbackQuery) -> None:
    await callback.answer('Вы выбрали 1200 руб')
    await callback.message.answer('Выберите способ пополнения', reply_markup=kb.replenishment1200)

@router.callback_query(F.data == '2400 руб')
async def cmd_2400(callback: CallbackQuery) -> None:
    await callback.answer('Вы выбрали 2400 руб')
    await callback.message.answer('Выберите способ пополнения', reply_markup=kb.replenishment2400)


