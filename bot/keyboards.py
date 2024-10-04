from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import get_logins
from kassa import create_payment, check_payment


def make_logins_kb(id) -> ReplyKeyboardMarkup: # Достаёт из бд логины стима на которые этот юзер тг делал пополнения 
    logins = []
    data = sorted(list(set(get_logins(id))))

    for i in range(len(data)):
        logins.append(KeyboardButton(text=data[i]))
    logins.append(cancel)

    return ReplyKeyboardMarkup(keyboard=[logins], 
                               resize_keyboard=True, input_field_placeholder="Введите/Выберите логин Steam...")


def ykReplenishment(payment):
    builder = InlineKeyboardBuilder()
    builder.button(text="Yookassa 8%", url=payment["confirmation"]["confirmation_url"]) # callback_data не работает вместе с url
    builder.button(text="Подтвердить платёж", callback_data="confirmation")
    builder.button(text="Отмена", callback_data="CancelPayment")
    return builder.adjust(1)


cancel = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отмена")]])

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Пополнение')],
                                    [KeyboardButton(text='Помощь')],
                                    [KeyboardButton(text='О нас'),
                                    KeyboardButton(text='Контакты')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

pomosh = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Не пришли средства на счёт', callback_data='Не пришли средства на счёт')],
                                               [InlineKeyboardButton(text='Проблемы с оплатой', callback_data='Проблемы с оплатой')],
                                               [InlineKeyboardButton(text='Проблемы в работе бота', callback_data='Проблемы в работе бота')],
                                               [InlineKeyboardButton(text='Другая проблема', callback_data='Другая проблема')]])
                                            # надо убрать нижние кнопки при вызове помощи и добавить сюда инлайн кнопку назад (для возвращения в меню)

contacts = InlineKeyboardMarkup(inline_keyboard=[])


