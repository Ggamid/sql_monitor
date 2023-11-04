import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

host = str(os.getenv("HOST"))
user = str(os.getenv("USER"))
password = str(os.getenv("PASSWORD"))
db_name = str(os.getenv("DB_NAME"))

host_REMOTE = str(os.getenv("HOST_REMOTE"))
host_R = str(os.getenv("HOST_R"))
user_R = str(os.getenv("USER_R"))
user_REMOTE = str(os.getenv("USER_REMOTE"))
password_R = str(os.getenv("PASSWORD_R"))
db_name_R = str(os.getenv("DB_NAME_R"))

admin_id = [
    635915647,
]
# admin_id[0] - GGAMID
