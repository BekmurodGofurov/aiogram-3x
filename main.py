import os
from aiogram import Bot, Dispatcher, F
from asyncio import run
from dotenv import load_dotenv
from functions import *

dp = Dispatcher()
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS = os.getenv('ADMINS')

async def start_up_navigation(bot: Bot):
    await bot.send_message(ADMINS, "Bot ishga tushdi✅")

async def shutdwon_navigation(bot: Bot):
    await bot.send_message(ADMINS, "Bot ishdan to'xtadi❕")    

async def start():
    dp.startup.register(start_up_navigation)

    dp.message.register(remove_markup, F.text.lower() == "cancel")
    dp.message.register(echo)

    dp.shutdown.register(shutdwon_navigation)

    bot = Bot(BOT_TOKEN)
    
    
    await dp.start_polling(bot)    
    
run(start())