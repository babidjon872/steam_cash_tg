import asyncio
from decouple import config
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
from kassa import create_payment, check_payment
#import logging


class Register(StatesGroup):
    login = State() # Сценарий ввода логина -> str
    amount = State() # Сценарий ввода суммы -> float
    method = State() # Сценарий метода оплаты -> str
    payment_id = State() # json ответ переработанный в dict -> dict
    waiting_msg_id = State() 
    payment_msg_id = State()



bot = Bot(token=config("TG_TOKEN"))
router = Router()
#logger = logging.getLogger(__name__)
#logging.basicConfig(filename="./logs/tgbot.log")


@router.message(F.text == "Отмена")
async def cancel(msg: types.Message, state: FSMContext) -> None:
    await state.clear()
    await msg.answer("Возвращаю в меню...", reply_markup=kb.main)


@router.callback_query(F.data == "CancelPayment")
async def cancel_payment(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.answer()
    await callback.message.answer("Возвращаю в меню...", reply_markup=kb.main)


@router.message(Register.login)
async def register_login(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(login=msg.text)
    #logger.warning(f"New steam login:'{msg.text}' from:{msg.from_user.id}")
    await msg.answer("Введите сумму пополнения в рублях", reply_markup=kb.cancel)
    await state.set_state(Register.amount)


@router.message(Register.amount)
async def reg_amount(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(amount=msg.text)
    data = await state.get_data()
    payment = await create_payment(data["login"], data["amount"])
    builder = kb.ykReplenishment(payment)
    payment_msg = await msg.answer("Оплата с помощью Yookassa:", reply_markup=builder.as_markup())
    await state.update_data(payment_msg_id=payment_msg.message_id)
    await state.set_state(Register.payment_id)
    await state.update_data(payment_id=payment["id"])
    msg = await msg.answer("Ожидаем оплату...")
    await state.update_data(waiting_msg_id=msg.message_id)


# Если не меняется статус платежа, то 
# обработать Bad Request: message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message
@router.callback_query(F.data == "confirmation")
async def wait_for_payment(callback_query: CallbackQuery, state: FSMContext) -> None:
    payment_id = await state.get_data()
    waiting_msg = payment_id["waiting_msg_id"]
    payment_msg = payment_id["payment_msg_id"]
    await callback_query.answer()
    if await check_payment(payment_id["payment_id"]):
        await bot.edit_message_text(text="Платёж прошёл успешно!\nДеньги в скором времени начислятся на ваш аккаунт...", 
                                    chat_id=callback_query.from_user.id, message_id=waiting_msg, reply_markup=kb.main)
        
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=payment_msg, request_timeout=1)
    else:
        await bot.edit_message_text(text="Ожидаем подтверждение платежа...", chat_id=callback_query.from_user.id, message_id=waiting_msg)

@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Приветствую", reply_markup=kb.main)
    await msg.answer("Что вас интересует?")
    new_user(msg.from_user.id, msg.from_user.username)
    # logger.info(f"New user tg_id:{msg.from_user.id}/date:{dt.datetime.now().strftime("%d.%m.%Y|%H:%M")}")


@router.message(F.text == 'Помощь')
async def cmd_help(msg: types.Message) -> None:
    await msg.answer('С чем возникла проблема?', reply_markup=kb.pomosh)


@router.message(F.text == 'Контакты')
async def cmd_help(msg: types.Message) -> None:
    await msg.answer('Создатель бота', reply_markup=kb.contacts)


@router.message(F.text == 'Пополнение')
async def cmd_replenishment(msg: types.Message, state: FSMContext) -> None:
    # print("Пополнениеyo")
    await msg.answer('Введите/Выберите логин аккаунта Steam', reply_markup=kb.cancel)
    # print("yo")
    await state.set_state(Register.login)
    # logger.info(f"User {msg.from_user.id} tries to replenish")


@router.message(F.text == 'О нас')
async def cmd_about(msg: types.Message) -> None:
    await msg.answer('Пока что данный раздел пуст')
