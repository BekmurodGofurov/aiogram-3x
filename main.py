import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from asyncio import run
from dotenv import load_dotenv
from functions import *
from filters import CheckSubChannel

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

  dp.message.register(sub_channel_answer, CheckSubChannel())
  dp.message.register(get_channel_id_answer, F.forward_from_chat)
  dp.message.register(echo)

  bot = Bot(BOT_TOKEN)
  await dp.start_polling(bot, polling_timeout=1)
run(start())