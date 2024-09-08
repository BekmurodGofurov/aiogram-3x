from aiogram import Bot, Dispatcher, F
from asyncio import run

import hanlder

dp=Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(your id, f"Bot is running")

async def shutdown_answer(bot: Bot):
    await bot.send_message(your id, f"bot stoped running")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    
    dp.include_router(hanlder.router)

    bot = Bot("Your bot token")
    await dp.start_polling(bot, polling_timeout=1)

run(start())        