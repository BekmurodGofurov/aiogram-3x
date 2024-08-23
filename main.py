import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from asyncio import run
from dotenv import load_dotenv
from functions import *
from states import get_user_real_name

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

  dp.message.register(start_command_answer, CommandStart())
  dp.message.register(get_realy_name_answer, get_user_real_name.name)
  dp.message.register(get_rf_id_answer, F.text == "Refferal havola")
  dp.message.register(get_user_ball_answer, F.text == "Mening ballarim")
  dp.shutdown.register(shutdwon_navigation)

  bot = Bot(BOT_TOKEN)
  await dp.start_polling(bot)
run(start())