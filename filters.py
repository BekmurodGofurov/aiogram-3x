from aiogram import Bot
from aiogram.filters import Filter
from aiogram .types import Message
from data import CHANNEL_ID

class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            return False
        return True 