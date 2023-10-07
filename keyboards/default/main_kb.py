from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from data.config import REPORN_AN_ACCIDENT, FIND_OUT_ACCIDENT, GET_PHONE
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)


main_kb.row(KeyboardButton(text=REPORN_AN_ACCIDENT),
            KeyboardButton(text=FIND_OUT_ACCIDENT),
            KeyboardButton(text=GET_PHONE))
