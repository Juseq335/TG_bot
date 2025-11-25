import asyncio 

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.base.database import async_main

# The most basic function that everything works on
async def main():
    await async_main()          # When the bot was launched, the creation of tables in the database began.
    bot = Bot(token='<your token>')
    disp = Dispatcher()
    disp.include_router(router) # Enabling routers
    await disp.start_polling(bot)

# Running the main function only if the main file is running.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('<your text>') # Changed the KeyboardInterrupt error to your text in the terminal
