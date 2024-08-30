from aiogram import Bot, Dispatcher, F
from asyncio import run
import functions
import callback_functions

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=your id, text="Bot starts working")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=your id, text="Bot stoped working!")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(functions.echo)
    dp.callback_query.register(callback_functions.day)

    bot = Bot("Your bot token")
    await dp.start_polling(bot, polling_timeout=1)

run(start())   