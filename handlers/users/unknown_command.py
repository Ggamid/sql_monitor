from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from SQL.wrk_db import get_access_level
from data.anabled_commands import available_commands



@dp.message_handler()
async def command_getId(message: types.Message):
    await message.answer(f"Неизвестная команда. Вот доступный вам список команд: {available_commands[get_access_level(message.from_user.id)]}")