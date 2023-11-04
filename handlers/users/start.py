from loader import dp
from aiogram import types
from SQL.wrk_db import get_status_db


@dp.message_handler(text='/start')
async def command_getId(message: types.Message):
    await message.answer(f"Hi 👋🏻, {message.from_user.full_name}. Я бот, который поможет"
                         f"тебе с администрированием БД👨🏻‍💼. it's your id - '{message.from_user.id}',"
                         f"сообщи его своему боссу, чтобы он добавил тебя как администратора"
                         f"и выдал тебе соответствующие права 🎫.")


@dp.message_handler(text='/get_stat')
async def command_getId(message: types.Message):
    text = get_status_db()
    await message.answer(f"Hi, {message.from_user.full_name}, status of db \n'{text}'")
