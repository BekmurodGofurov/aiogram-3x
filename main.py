from aiogram import Bot, Dispatcher, F
from aiogram.filters import and_f
from asyncio import run
import functions
dp=Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(your id , f"Bot is running")

async def shutdown_answer(bot: Bot):
    await bot.send_message(your id, f"bot stoped running")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(functions.new_chat_members_answer, and_f(F.chat.id == -1002233391717, F.new_chat_members))
    dp.message.register(functions.left_chat_member_answer, and_f(F.chat.id == -1002233391717, F.left_chat_member))
    dp.message.register(functions.get_info, F.chat.id != -1002233391717)

    dp.message.register(functions.mute_member_answer, and_f(F.chat.type =="supergroup", and_f(F.text == "/mute", F.reply_to_message)))
    dp.message.register(functions.unmute_member_answer, and_f(F.chat.type =="supergroup", and_f(F.text == "/unmute", F.reply_to_message)))
    dp.message.register(functions.ban_member_answer, and_f(F.chat.type =="supergroup", and_f(F.text == "/ban", F.reply_to_message)))
    dp.message.register(functions.unban_member_answer, and_f(F.chat.type =="supergroup", and_f(F.text == "/unban", F.reply_to_message)))

    bot = Bot("Your bot token")
    await dp.start_polling(bot, polling_timeout=1)

run(start())        