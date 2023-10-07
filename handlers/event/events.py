
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup
from keyboards.default.cancel import cancel
from keyboards.inline.else_months import else_months
from loader import dp
from states.states import EventState
from utils.misc.throttling import rate_limit
from utils.mongo.events_class import Events
from utils.mongo.user_class import User
from datetime import datetime
from .print_events import print_events


@rate_limit(3, '✏️Редактировать мероприятие')
@dp.message_handler(Text(equals="✏️Редактировать мероприятие"), state='*')
async def edit_event(message: Message, keyboard: ReplyKeyboardMarkup, is_admin: bool = False):
    events = await Events.get_all_future_events(is_admin=is_admin)
    if not events:
        await message.answer(f'{message.from_user.full_name}, ещё нет предстоящих мероприятий\!', reply_markup=keyboard)
    await print_events(message=message, events=events, edit=True, is_admin=is_admin)
    await message.answer(f'👇Все мероприятия👇', reply_markup=else_months(edit=True))


@rate_limit(3, '📥Моё участие📥')
@dp.message_handler(Text(equals='📥Моё участие📥'), state='*')
async def my_events(message: Message, keyboard: ReplyKeyboardMarkup, is_admin: bool = False):
    # events = await Events.get_my_future_events(user_id=message.from_user.id, is_admin=is_admin)
    # # await message.answer("Please select a date: ", reply_markup=await DialogCalendar().start_calendar())

    # await print_events(message, events, edit=False, is_admin=is_admin)
    # await message.answer('Все мероприятия *в которых вы участвовали* за последний месяц\.', reply_markup=keyboard)
    user = await User(user_id=message.chat.id).get_info()
    all_my_events = await Events.get_all_my(
        user_id=message.chat.id,
        is_admin=user.get('is_admin')
    )
    if not all_my_events:
        return await message.answer('Вы пока не участвуете ни в каком мероприятии\.', reply_markup=keyboard)
    # if not else_events:
    #     await message.answer('До этого мероприятий не было!')
    my_events_dict = {}
    # Сортируем по годам
    for event in all_my_events:
        event_datetime = datetime.utcfromtimestamp(event.get('timestamp'))
        year = event_datetime.year
        try:
            my_events_dict[year].append(event)
        except:
            my_events_dict[year] = [event]
    for event_year, events in my_events_dict.items():
        keyboard = InlineKeyboardMarkup()
        for event in events:
            keyboard.row(KeyboardButton(event.get('title'), callback_data=f'event_{event.get("_id")}'))
        await message.answer(f'*{event_year}*', reply_markup=keyboard)

    # await message.answer(f'👇Вск мероприятия в которых ты участвовал👇', reply_markup=else_months(my=message.from_user.id))


@rate_limit(3, '🎭Мероприятия')
@dp.message_handler(Text(equals="🎭Мероприятия"), state='*')
async def events(message: Message, keyboard: ReplyKeyboardMarkup, is_admin: bool):
    events = await Events.get_all_future_events(is_admin=is_admin)
    if not events:
        if not await Events.get_all(is_admin=is_admin):
            return await message.answer(f'{message.from_user.full_name}, ещё нет созданных мероприятий\!',
                                        reply_markup=keyboard)
        await message.answer(f'{message.from_user.full_name}, ещё нет предстоящих мероприятий\!',
                             reply_markup=keyboard)
        return await message.answer(f'👇Все мероприятия👇', reply_markup=else_months())
    await print_events(message, events, edit=False, is_admin=is_admin)
    await message.answer('Все предстоящие мероприятия', reply_markup=keyboard)
    await message.answer(f'👇Все мероприятия👇', reply_markup=else_months())


@dp.message_handler(Text(equals="📍Добавить мероприятие"), state="*")
async def add_events(message: Message):
    await message.answer('Введи название мероприятия', reply_markup=cancel(add=True))
    await EventState.title.set()
