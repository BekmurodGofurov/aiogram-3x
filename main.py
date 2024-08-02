from aiogram import Bot, Dispatcher, types
from asyncio import run

dp = Dispatcher()

async  def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

async def start():
    dp.message.register(echo)

    bot = Bot("5826284002:AAH8Hld-eqgotaxlmL7-QImA14vtyIEhAnY")
    await dp.start_polling(bot)    
    print("It is polling")

run(start())