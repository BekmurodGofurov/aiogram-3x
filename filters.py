from aiogram.filters import Filter
from aiogram.types import Message

class text_ichda_bormi(Filter):
    def __init__(self, text_list: list):
        self.text_list = text_list

    async def __call__(self, message: Message):
        return message.text in self.text_list    