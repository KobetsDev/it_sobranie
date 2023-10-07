from aiogram.dispatcher import FSMContext

from keyboards.default.cancel import cancel
from keyboards.inline.pick_area import area_ikb
from loader import dp
from states.states import AccidentState
from aiogram.types import CallbackQuery
from data.config import RESULT_FORM

@dp.callback_query_handler(text_startswith='pick_resource_', state=AccidentState.resource)
async def resource_callback_handler(query: CallbackQuery, state: FSMContext):
    '''Выбор типа происшествия'''
    resource: str = query.data.split('_')[2]
    async with state.proxy() as data:
            data['resource'] = resource
    
    await query.message.answer('Укажите район', reply_markup=area_ikb())
    await AccidentState.next()


@dp.callback_query_handler(text_startswith='pick_area_', state=AccidentState.area)
async def area_callback_handler(query: CallbackQuery, state: FSMContext):
    '''Выбор район'''
    area: str = query.data.split('_')[2]

    async with state.proxy() as data:
        data['area'] = area
    await query.answer(' ')
    await query.message.answer('Укажите улицу и дом', reply_markup=cancel(add=True))
    await AccidentState.next()

@dp.callback_query_handler(text_startswith='skip', state=AccidentState.description)
async def area_callback_handler(query: CallbackQuery, state: FSMContext):
    '''Выбор район'''
    async with state.proxy() as data:
        data['description'] = ''
    await query.message.answer(
            f'Всё правильно?\n{RESULT_FORM.format(data["resource"],data["area"],data["address"],data["description"])}', 
            reply_markup=cancel(add=True))
    await AccidentState.next()
