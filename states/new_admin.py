from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    get_ID = State()
    get_access_level = State()
    confirmation = State()

