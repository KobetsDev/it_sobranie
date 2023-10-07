from aiogram.types import InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

def phone_ikb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for prone in ['+7 999 888 73 32', '+7 999 888 73 32', '+7 999 888 73 32']:
        keyboard.add(KeyboardButton(prone, callback_data=''))
    return keyboard
