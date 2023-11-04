from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    get_ID = State()
    get_access_level = State()
    confirmation = State()


class OwnRequest(StatesGroup):
    getText = State()
    confirmation = State()


class AdminDelete(StatesGroup):
    getID = State()
    confirmation = State()


class TruncateData(StatesGroup):
    getTable = State()
    confirmation = State()
