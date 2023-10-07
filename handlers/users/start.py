import random

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
# from keyboards.default.admin_kb import admin_kb
from keyboards.default.main_kb import main_kb
# from keyboards.default.register_kb import register_kb
from loader import dp
from utils.misc.throttling import rate_limit
from utils.mongo.user_class import User
from data.config import START_FORM

# @rate_limit(3, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать о великий\!\n{START_FORM}', reply_markup=main_kb)
