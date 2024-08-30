from aiogram.types import Message
from keyboards import builder
async def echo(message: Message):
    await message.copy_to(message.chat.id, reply_markup=builder)