from aiogram.types import InlineKeyboardMarkup, KeyboardButton
from data.config import RESOURCE_LIST

def resource_ikb() -> InlineKeyboardMarkup:
    '''Клавиатура для выбора типа происшествия'''
    keyboard = InlineKeyboardMarkup(row_width=1)
    for resource in RESOURCE_LIST:
        keyboard.add(KeyboardButton(resource, callback_data=f'pick_resource_{resource}'))
    return keyboard
