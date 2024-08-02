from aiogram import Bot, Dispatcher, types
from asyncio import run

dp = Dispatcher()

async def start_up_navigation(bot: Bot):
    await bot.send_message(5841656536, "Bot ishga tushdi✅")

async def shutdwon_navigation(bot: Bot):
    await bot.send_message(5841656536, "Bot ishdan to'xtadi❕")    

async  def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

async def start():
    dp.startup.register(start_up_navigation)
    dp.message.register(echo)
    dp.shutdown.register(shutdwon_navigation)

    bot = Bot("5826284002:AAH8Hld-eqgotaxlmL7-QImA14vtyIEhAnY")
    await dp.start_polling(bot)    

run(start())