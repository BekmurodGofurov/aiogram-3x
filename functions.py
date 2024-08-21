from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import reply_button

async def echo(message: Message):
    await message.copy_to(message.chat.id, reply_markup=reply_button)

async def remove_markup(message: Message):
    await message.answer("Markup tozalandi!", reply_markup=ReplyKeyboardRemove())
