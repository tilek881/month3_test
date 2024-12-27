import asyncio


from bot_config import manager ,dp , bot
from handlers.start import start_router
from handlers.complant import complaint_router



async def on_startup(bot):
    manager.create_tables()

async def main():

    dp.include_router(start_router)
    dp.include_router(complaint_router)

    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())