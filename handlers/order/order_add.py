
import logging

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.inline.dialog_calendar_add_order import DialogCalendarAddOrder
from loader import dp
from states.states import OrderState
from utils.misc.throttling import rate_limit
from utils.mongo.orders_class import Orders


@rate_limit(3, '🖌Добавить распоряжение')
@dp.message_handler(Text(equals="🖌Добавить распоряжение"), state='*')
async def add_order(message: Message):
    '''Добавляем распоряжение'''
    await message.answer('Выберите месяц за который надо добавить ссылку на распоряжение',
                         reply_markup=await DialogCalendarAddOrder().start_calendar())
    await OrderState.date.set()


@dp.message_handler(state=OrderState.link)
async def order_link(message: Message, state: FSMContext):
    link: str = message.text.strip()
    if not (link.startswith('http://') or link.startswith('https://')):
        return await message.answer('Вы ввели не ссылку, повторите пожалуйста')
    order = await state.get_data()
    year: int = order.get('date').year
    month: int = order.get('date').month
    if await Orders.add_order(order={
        'year': year,
        'month': month,
        'link': link
    }):
        await message.answer('Распоряжение успешно добавлено')
    else:
        logging.error('orderLinkAdd', message)
        await message.answer('Ошибка')
    await state.finish()
