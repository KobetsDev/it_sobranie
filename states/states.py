# from aiogram.utils.helper import Helper, HelperMode, ListItem, Item
from aiogram.dispatcher.filters.state import State, StatesGroup


class AccidentState(StatesGroup):
    resource = State()
    area = State()
    address = State()
    description = State()
    check = State()

class GetAccidentState(StatesGroup):
    get_address = State()

