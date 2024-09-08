from aiogram.types import Message
from aiogram import Bot

async def ban_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"]:
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            await message.chat.ban_sender_chat(ban_user.id)
            await message.answer(f"{ban_user.full_name} gruhdan blocklandi")
        else:
            await message.answer("Kimnidur blocklarsh uchun siz uni hxabariga replay qilishingiz kerak")
        
    else:
        await message.reply("Siz gruhda admin emsiz foydalanuchilarni blocklash uchun.")
    
async def unban_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"]:
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            await message.chat.unban_sender_chat(ban_user.id)
            await message.answer(f"{ban_user.full_name} blockdan chiqdi")
        else:
            await message.answer("Kimnidur blockdan olish uchun siz userni hxabariga replay qilishingiz kerak")
        
    else:
        await message.reply("Siz gruhda admin emsiz foydalanuchilarni blockdan olish uchun.")
