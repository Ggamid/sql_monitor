from loader import dp
from aiogram import types
from SQL.wrk_db import get_access_level
from data.anabled_commands import available_commands


@dp.message_handler(text='/start')
async def command_getId(message: types.Message):
    await message.answer(f"Hi 👋🏻, {message.from_user.full_name}. Я бот, который поможет "
                         f"тебе с администрированием БД👨🏻‍💼. it's your id - '{message.from_user.id}', "
                         f"сообщи его своему боссу, чтобы он добавил тебя как администратора "
                         f"и выдал тебе соответствующие права 🎫. \n \n вот доступный вам список команд👇🏻\n\n"
                         f"{available_commands[get_access_level(message.from_user.id)]}")


