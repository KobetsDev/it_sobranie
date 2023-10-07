
from aiogram.utils.markdown import escape_md
import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.utils.exceptions import FileIsTooBig
# from data.config import CONTACT
# from data.config import EVENT_FORM
from keyboards.default.cancel import cancel
from keyboards.inline.dialog_calendar import DialogCalendar
from keyboards.inline.pick_area import area_ikb
from keyboards.inline.skip import skip_ikb
from loader import dp
from states.states import AccidentState, GetAccidentState
# from utils.human_datetime import get_datetime, humanize_datetime
from utils.mongo.events_class import Events
from data.config import RESULT_FORM


@dp.message_handler(Text(equals='Отменить создание', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext, keyboard: ReplyKeyboardMarkup):
    """Отменяем ввод данных для мероприятия"""
    current_state = await state.get_state()
    if current_state is None:
        return await message.reply('Пасхалка 1/3\!', reply=False, reply_markup=keyboard)
    await state.finish()
    await message.reply('ОК', reply=False, reply_markup=keyboard)


@dp.message_handler(state=AccidentState.address)
async def accident_address(message: Message, state: FSMContext):
    """Адрес происшествия"""
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer(f'Опишите что произошло\(не обязательно\)', reply_markup=skip_ikb())
    await AccidentState.next()

@dp.message_handler(state=GetAccidentState.get_address)
async def accident_address(message: Message, state: FSMContext):
    """Адрес происшествия"""
    async with state.proxy() as data:
        data['get_address'] = message.text
    await message.answer('По этому адресу нет происшествий')


@dp.message_handler(state=AccidentState.description)
async def accident_description(message: Message, state: FSMContext):
    """Описание происшествия"""
    async with state.proxy() as data:
        data['description'] = message.text
        await message.answer(
            f'Всё правильно?\n{RESULT_FORM.format(data["resource"],data["area"],data["address"],data["description"])}', reply_markup=cancel(with_ok=True))
    await AccidentState.next()

@dp.message_handler(state=AccidentState.check)
async def event_check(message: Message, state: FSMContext, keyboard: ReplyKeyboardMarkup):
    """Проверка сообщения инцидента перед отправкой"""
    if 'да' == (message.text).lower():
        await message.answer(f'Ваше обращение зафиксированно.\nВ ближайшее время мы решим ваш вопрос.', reply_markup=keyboard)

    else:
        await message.answer('Данные сброшены', reply_markup=keyboard)
    await state.finish()