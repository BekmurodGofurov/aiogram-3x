from aiogram.filters import Filter
from aiogram.types import Message

class isAd(Filter):
    async def __call__(self, message: Message):
        if message.text:
            if "@" in message.text or "https://" in message.text or "T.me" in message.text:
                return True
        elif message.caption:
            if "@" in message.caption or "https://" in message.caption or "T.me" in message.caption:
                return True