from aiogram.types import Message

async def start(message: Message):
    await message.reply(F'Salom {message.from_user.first_name}')