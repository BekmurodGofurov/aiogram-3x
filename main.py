from aiogram import Bot, Dispatcher, F
from asyncio import run
import callback_functions
import functions

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id="your id", text=f"Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id="your id", text="Bot ishdan to'xtadi ❌")    

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(functions.echo)
    dp.callback_query.register(callback_functions.ok_action, F.data=="ok")
    
    bot = Bot("Your bot token")