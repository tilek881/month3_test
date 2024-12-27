import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from handlers.start import start_router


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()



async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())