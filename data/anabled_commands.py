senior_commands = """

/add_admin - добавление нового администратора 👨🏻‍💼

/truncate_data - удаление данных из таблицы  ❌

/sent_own_request - отпаравление собственного запроса в БД 📞

/my_commands - посмотреть доступных мне команд  👁️

/delete_admin - удалить администратора БД ␡

/get_admins - список всех админов и их уровень доступа ⚡️

/get_list_tables - список всех таблиц в БД 📋

/create_table - создание таблицы с нужными столбцами
"""
midle_commands = """
/my_commands - посмотреть доступных мне команд
"""
junior_commands = """
/my_commands - посмотреть доступных мне команд
"""
unkonown_user = """

/get_list_tables - список всех таблиц в БД 📋

"""

available_commands = {"Senior" : senior_commands, "Midle" : midle_commands, "Junior" : junior_commands, "пользователя нет в бд" : unkonown_user}
