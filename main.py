import os
from aiogram import Bot, Dispatcher, F
from asyncio import run
from dotenv import load_dotenv
import functions
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
  dp.shutdown.register(shutdwon_navigation)

  dp.message.register(functions.echo  )

  bot = Bot(BOT_TOKEN)
  await dp.start_polling(bot, polling_timeout=1)
run(start())