from aiogram import types


async def set_default_commands(dp):
    await dp.set.set_my_commands([
        types.BotCommand('startSquadViceGAA'),
        types.BotCommand('lastMessage', 'Последнее уведомление')
    ])
