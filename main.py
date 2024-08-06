import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.filters import Command
from asyncio import run
from dotenv import load_dotenv
from functions import *
from states import sign_up

dp = Dispatcher()
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS = os.getenv('ADMINS')

async def start_up_navigation(bot: Bot):
    await bot.send_message(ADMINS, "Bot ishga tushdi✅")

async def shutdwon_navigation(bot: Bot):
    await bot.send_message(ADMINS, "Bot ishdan to'xtadi❕")    

# async  def echo(message: types.Message, bot: Bot):
#     await message.copy_to(chat_id=message.chat.id)

async def start():
    dp.startup.register(start_up_navigation)

    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))

    dp.message.register(sign_up_name, sign_up.name)
    dp.message.register(sign_up_age, sign_up.age)

    dp.message.register(get_user_info)
    dp.shutdown.register(shutdwon_navigation)

    bot = Bot(BOT_TOKEN)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish" ),
        BotCommand(command="/help", description="Yordam olish" ),
    ])
    
    await dp.start_polling(bot)    
    
run(start())