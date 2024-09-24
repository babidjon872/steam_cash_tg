from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Пополнение')],
                                     [KeyboardButton(text='Помощь')],
                                     [KeyboardButton(text='О нас'),
                                      KeyboardButton(text='Контакты')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выбери пункт меню...')

pomosh = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Не пришли средства на счёт', callback_data='Не пришли средства на счёт')],
                                               [InlineKeyboardButton(text='Проблемы с оплатой', callback_data='Проблемы с оплатой')],
                                               [InlineKeyboardButton(text='Проблемы в работе бота', callback_data='Проблемы в работе бота')],
                                               [InlineKeyboardButton(text='Другая проблема', callback_data='Другая проблема')]])


replenishment = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='300 руб', callback_data='300 руб'),
                                                       InlineKeyboardButton(text='600 руб', callback_data='600 руб')],
                                                      [InlineKeyboardButton(text='1200 руб', callback_data='1200 руб'),
                                                       InlineKeyboardButton(text='2400 руб', callback_data='2400 руб')]])

replenishment300 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СБП', callback_data='СБП')],
                                                         [InlineKeyboardButton(text='Сбер', callback_data='Сбер')],
                                                         [InlineKeyboardButton(text='Т-Банк', callback_data='Т-Банк')]])


replenishment600 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СБП', callback_data='СБП')],
                                                         [InlineKeyboardButton(text='Сбер', callback_data='Сбер')],
                                                         [InlineKeyboardButton(text='Т-Банк', callback_data='Т-Банк')]])


replenishment1200 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СБП', callback_data='СБП')],
                                                         [InlineKeyboardButton(text='Сбер', callback_data='Сбер')],
                                                         [InlineKeyboardButton(text='Т-Банк', callback_data='Т-Банк')]])



replenishment2400 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СБП', callback_data='СБП')],
                                                         [InlineKeyboardButton(text='Сбер', callback_data='Сбер')],
                                                         [InlineKeyboardButton(text='Т-Банк', callback_data='Т-Банк')]])

get_name = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправьте имя аккаунта в чат')]], resize_keyboard=True)


