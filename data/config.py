import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

host = str(os.getenv("HOST"))
user = str(os.getenv("USER"))
password = str(os.getenv("PASSWORD"))
db_name = str(os.getenv("DB_NAME"))

admin_id = [
    635915647,
]
# admin_id[0] - GGAMID
