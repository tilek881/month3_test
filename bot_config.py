from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from handlers.complant import manager_db
from manager_db import Database


token= dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


manager = Database("complaints.db")
manager_db.create_tables()

