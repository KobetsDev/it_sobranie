
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.inline.dialog_calendar_remove_order import \
    DialogCalendarRemoveOrder
from loader import dp
from utils.misc.throttling import rate_limit


@rate_limit(3, '🗑Удалить распоряжение')
@dp.message_handler(Text(equals='🗑Удалить распоряжение'), state='*')
async def remove_order(message: types.Message):
    '''Удаляем распоряжение'''
    await message.answer('Выберите месяц за который надо *удалить* ссылку на распоряжение',
                         reply_markup=await DialogCalendarRemoveOrder().start_calendar())
