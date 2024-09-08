from aiogram import Bot
from aiogram.types import Message

async def get_ads_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ("administrator", "creator"): return
    else:
        await message.delete()
        await message.answer(f"{message.from_user.full_name} iltimos reklama tarqatmang!")
    