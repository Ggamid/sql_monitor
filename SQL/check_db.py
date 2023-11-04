from data.config import host_R as host, user_R as user, password_R as password, db_name_R as db_name, host_REMOTE, \
    user_REMOTE
from aiogram import Dispatcher
from loader import bot
import psycopg2
from sshtunnel import SSHTunnelForwarder
from SQL.wrk_db import get_admins
import asyncio
from time import sleep

server = SSHTunnelForwarder((host_REMOTE, 22), ssh_username=user_REMOTE,
                            ssh_password=password,
                            remote_bind_address=("localhost", 5432))


server.start()
connect_data = {"dbname": db_name,
                "user": user,
                "host": 'localhost',
                "password": password,
                "port": server.local_bind_port}


async def check_database_status():
    try:
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                cur.execute(f"SELECT version();")
                result = cur.fetchone()
                status_text = f"База данных работает. Версия PostgreSQL: {result[0]}"

        # admin_list = [635915647]
        # for tg_id in admin_list:
        #     await bot.send_message(tg_id, f"{status_text}")

    except psycopg2.Error as e:
        status_text = f"Ошибка при выполнении SQL-запроса: {e}"
        admin_list = [635915647]
        for tg_id in admin_list:
            await bot.send_message(tg_id, f"{status_text}")
        sleep(15)




