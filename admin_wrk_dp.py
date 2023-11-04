import psycopg2
from data.config import host, user, password, db_name


def create_admin_table():
    try:
        table = """
        CREATE TABLE IF NOT EXISTS admin_table(
            startCommand TEXT
        );
        """
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(table)

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


def addStartCommand(command):
    try:

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"insert into admin_table(startCommand) Values(%s)", [command])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def getStartCommand():
    try:
        list_start_command = []
        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"select startCommand from admin_table")

                for row in cur.fetchall():
                    list_start_command.append(row[0])

        return list_start_command
    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


def deleteStartCommand(command):
    try:

        with psycopg2.connect(host=host, user=user, password=password, database=db_name) as con:
            with con.cursor() as cur:
                cur.execute(f"delete from admin_table startCommand where startCommand = %s", [command])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)


create_admin_table()