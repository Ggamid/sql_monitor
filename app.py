from aiogram import executor
from handlers import dp


async def on_start_up(dp):
    from utils.notify_admins import on_start_up_notify
    await on_start_up_notify(dp)

    print("Bot is started")


if __name__ == "__main__":

    executor.start_polling(dp, on_start_up=on_start_up())

    # executor.start_polling(dp, on_startup=on_start_up)
