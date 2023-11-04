import psycopg2
from data.config import host, user, password, db_name
from aiogram import Dispatcher


def create_table():
    try:
        table = """
        CREATE TABLE IF NOT EXISTS admin_data(
            tg_id BIGINT,
            acces_level TEXT
        );
        """
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(table)

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def drop_data_in_table():
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("TRUNCATE TABLE vice_squad")
        return True
    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)
        return False


def drop_table():
    try:

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("DROP TABLE vice_squad")

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def reg_tg_id(tg_id):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"select tg_id from vice_squad where tg_id = %s", [tg_id])
                if cur.fetchone() is not None:
                    print("[INFO] такой пользователь уже в БД")
                else:
                    cur.execute(f"insert into vice_squad(tg_id) values(%s)",
                                [tg_id])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def add_human(tg_id, name, numClass):
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute(f"update vice_squad set name = %s, num_of_class = %s where tg_id = %s",
                            [name, numClass, tg_id])
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def check_connect():
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select * from users")
                for row in cur.fetchall():
                    print(row[0])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_count_wrong_right(tg_id) -> []:
    try:
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select count_right, count_wrong from users where tg_id = %s", [tg_id])
                ls = []
                for row in cur.fetchall():
                    ls.append(row[0])
                    ls.append(row[1])
                return ls


    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_id_users():
    try:
        list_id_users = []
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select tg_id from vice_squad")

                for row in cur.fetchall():
                    list_id_users.append(row[0])

        return list_id_users
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_stat():
    try:
        list_of_users = []

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select tg_id from users")

                for row in cur.fetchall():
                    list_of_users.append(row[0])

        return [len(list_of_users)]
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def get_status_db():
    try:
        list_of_connect = []

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                # Запрос для получения информации о текущих активных сеансах
                query = "SELECT * FROM pg_stat_activity"

                # Выполнение запроса
                cur.execute(query)
                rows = cur.fetchall()
                # Вывод информации о текущих активных сеансах
                for row in rows:
                    list_of_connect.append(row)

        return list_of_connect[0]
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)



# # 635915647
create_table()
# drop_table()
