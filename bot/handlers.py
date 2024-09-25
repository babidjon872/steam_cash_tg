import asyncio
import datetime as dt
from db import new_payment, new_user # функции взаимодействия с бд
from aiogram import Bot, Dispatcher, types
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
import keyboards as kb
from keyboards import make_logins_kb # функция для нахождения логинов стима в бд
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import logging


class Register(StatesGroup):
    login = State() # Сценарий ввода логина -> str
    amount = State() # Сценарий ввода суммы -> float
    method = State() # Сценарий метода оплаты -> str

router = Router()
logger = logging.getLogger(__name__)
logging.basicConfig(filename="./logs/tgbot.log")


@router.message(F.text == "Отмена")
async def cancel(msg: types.Message, state: FSMContext) -> None:
    await state.clear()


@router.message(Register.login)
async def register_login(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(login=msg.text)
    print(msg.text)
    logger.warning(f"New steam login:'{msg.text}' from:{msg.from_user.id}")
    await state.set_state(Register.amount)


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Приветствую", reply_markup=kb.main)
    await msg.answer("Что вас интересует?")
    new_user(msg.from_user.id, msg.from_user.username)
    # logger.info(f"New user tg_id:{msg.from_user.id}/date:{dt.datetime.now().strftime("%d.%m.%Y|%H:%M")}")



@router.message(F.text == 'Помощь')
async def cmd_help(msg: types.Message) -> None:
    await msg.answer('С чем возникла проблема?', reply_markup=kb.pomosh)


@router.message(F.text == 'Пополнение')
async def cmd_replenishment(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(Register.login)
    await msg.answer('Введите/Выберите логин аккаунта Steam', reply_markup=make_logins_kb(msg.from_user.id))
    # logger.info(f"User {msg.from_user.id} tries to replenish")


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


