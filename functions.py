from aiogram import Bot
from aiogram.types import  Message

async def get_channel_id_answer(message: Message):
    await message.answer(f"Kanal ID: {message.forward_from_chat.id}")

async def echo(message: Message):
    await message.copy_to(message.chat.id)    

async def sub_channel_answer(message: Message):
    invite_link = "https://t.me/Bekmurod_Gofurov"
    await message.answer(f"Iltimos kanalga obuna bo'ling!\n\n<a href='{invite_link}'>Link</a>", parse_mode="HTML")    