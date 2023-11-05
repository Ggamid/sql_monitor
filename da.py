import asyncio
import aioschedule as schedule
from aiogram import executor
from SQL.check_db import check_database_status
from handlers import dp

import handlers


async def scheduler():
    schedule.every(15).seconds.do(check_database_status)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)