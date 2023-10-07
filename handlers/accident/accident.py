
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from keyboards.default.cancel import cancel
from keyboards.inline.pick_phone import phone_ikb
from keyboards.inline.pick_resource import resource_ikb
from loader import dp
from states.states import AccidentState, GetAccidentState
from data.config import REPORN_AN_ACCIDENT, GET_PHONE, FIND_OUT_ACCIDENT

# @rate_limit(3, '✏️Редактировать мероприятие')
@dp.message_handler(Text(equals=REPORN_AN_ACCIDENT), state='*')
async def take_accident(message: Message): #, keyboard: ReplyKeyboardMarkup
    
    await message.answer('Выберите тип инцидента', 
                         reply_markup=resource_ikb()
                        #  reply_markup=cancel(add=True)
                         )
    print('take_accident')
    await AccidentState.resource.set()


@dp.message_handler(Text(equals=GET_PHONE), state='*')
async def take_accident(message: Message):
    
    await message.answer('Телефон службы', 
                         reply_markup=phone_ikb())
    await AccidentState.resource.set()


@dp.message_handler(Text(equals=FIND_OUT_ACCIDENT), state='*')
async def take_accident(message: Message):
    
    await message.answer('Введите ваш адресс')
    await GetAccidentState.get_address.set()
