from aiogram.types import InlineKeyboardMarkup, KeyboardButton
from data.config import RESOURCE_LIST

def skip_ikb() -> InlineKeyboardMarkup:
    '''Клавиатура пропуска описания инфидента'''
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(KeyboardButton('Пропустить', callback_data=f'skip'))
    return keyboard
