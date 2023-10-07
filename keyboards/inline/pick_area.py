from aiogram.types import InlineKeyboardMarkup, KeyboardButton
from data.config import AREA_LIST

def area_ikb() -> InlineKeyboardMarkup:
    '''Клавиатура для выбора рыйона'''
    keyboard = InlineKeyboardMarkup(row_width=len(AREA_LIST))
    for area in AREA_LIST:
        keyboard.add(KeyboardButton(area, callback_data=f'pick_area_{area}'))
    return keyboard
