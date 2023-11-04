import psycopg2
from data.config import host_R as host, user_R as user, password_R as password, db_name_R as db_name, host_REMOTE, \
    user_REMOTE
from aiogram import Dispatcher
import psycopg2
from sshtunnel import SSHTunnelForwarder
import asyncio

server = SSHTunnelForwarder((host_REMOTE, 22), ssh_username=user_REMOTE,
                            ssh_password=password,
                            remote_bind_address=("localhost", 5432))

server.start()

connect_data = {"dbname": db_name,
                "user": user,
                "host": 'localhost',
                "password": password,
                "port": server.local_bind_port}


def create_table():
    try:
        table = """
        CREATE TABLE IF NOT EXISTS admin_data(
            tg_id BIGINT,
            access_level TEXT
        );
        """
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                cur.execute(table)

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def drop_data_in_table(table):
    try:
        with psycopg2.connect(**connect_data) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"TRUNCATE TABLE {table}")
        return True
    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)
        return False


def drop_table():
    try:

        with psycopg2.connect(**connect_data) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("DROP TABLE test")
            print("table droped")

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def reg_tg_id(tg_id, acces_level):
    try:
        with psycopg2.connect(**connect_data) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"select tg_id from admin_data where tg_id = %s", [tg_id])
                if cur.fetchone() is not None:
                    print("[INFO] такой пользователь уже в БД")
                else:
                    cur.execute(f"insert into admin_data(tg_id, access_level) values(%s, %s)",
                                [tg_id, acces_level])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


# def add_human(tg_id, access_level):
#     try:
#         with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
#             con.autocommit = True
#             with con.cursor() as cur:
#                 cur.execute(f"insert into admin_data set tg_id = %s, acces_level = %s",
#                             [tg_id, access_level])
#     except psycopg2.Error as _ex:
#         print("[INFO]", _ex)


def check_connect():
    try:
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                cur.execute(f"select * from users")

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_access_level(tg_id) -> []:
    try:
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                cur.execute(f"select access_level from admin_data where tg_id = %s", [tg_id])
                return cur.fetchall()[0][0]

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_admins():
    try:
        list_id = ""
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                cur.execute(f"select * from admin_data")
                # print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
                for row in cur.fetchall():
                    # f"{row[0]} : {row[1]} \n",
                    list_id += f'{row[0]:10d} : {row[1]:10s}\n'

        return list_id
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


# def get_stat():
# try:
#     list_of_users = []
#
#     with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
#         with con.cursor() as cur:
#             cur.execute(f"select tg_id from users")
#
#             for row in cur.fetchall():
#                 list_of_users.append(row[0])
#
#     return [len(list_of_users)]
# except psycopg2.Error as _ex:
#     print("[INFO]", _ex)


def get_status_db():
    try:
        list_of_connect = []

        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                # Запрос для получения информации о текущих активных сеансах
                query = "SELECT * FROM pg_stat_activity"

                # Выполнение запроса
                cur.execute(query)
                rows = cur.fetchall()
                # Вывод информации о текущих активных сеансах
                for row in rows:
                    list_of_connect.append(row)

        return list_of_connect
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def sent_own_requets(text):
    try:
        result = ""
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                # Запрос для получения информации о текущих активных сеансах
                query = text

                # Выполнение запроса
                cur.execute(query)
                return cur.fetchall()

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)
        return f"[INFO] {_ex}"


def get_list_tables():
    try:
        result = ""
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                # Запрос для получения информации о текущих активных сеансах
                query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
                """

                # Выполнение запроса
                cur.execute(query)
                for row in cur.fetchall():
                    result += "\n" + row[0]
                return result

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)
        return f"[INFO] {_ex}"


def delete_admin(tg_id):
    try:
        with psycopg2.connect(**connect_data) as con:
            with con.cursor() as cur:
                # Запрос для получения информации о текущих активных сеансах
                query = "DELETE FROM admin_data WHERE tg_id = %s;"

                # Выполнение запроса
                cur.execute(query, [tg_id])
                return cur.fetchall()

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)
        return f"[INFO] {_ex}"

# print(get_list_tables())
# # 635915647
# drop_table()
# create_table()
# drop_table()
