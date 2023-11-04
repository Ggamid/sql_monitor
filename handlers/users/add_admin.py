from loader import dp
from aiogram import types
from wrk_db import get_status_db


@dp.message_handler(text='\add_admin')
async def command_getId(message: types.Message):
    await message.answer(f"")


@dp.message_handler(text='/get_stat')
async def command_getId(message: types.Message):
    text = get_status_db()
    await message.answer(f"Hi, {message.from_user.full_name}, status of db \n'{text}'")
