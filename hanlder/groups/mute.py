from aiogram import Bot
from aiogram.types import Message, ChatPermissions


async def mute_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"]:
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            permissions = ChatPermissions(can_send_messages=False)
            await message.chat.restrict(user.id, permissions)
            await message.answer(f"{user.full_name} endi yoza olmaydi.")
        else:
            await message.answer("Kimnidur mute uchun siz uni hxabariga replay qilishingiz kerak")
    else:
        await message.reply("Siz gruhda admin emsiz foydalanuchilarni mute qilish uchun.")


async def unmute_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"]:
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            permissions = ChatPermissions(can_send_messages=True, can_invite_users=True)
            await message.chat.restrict(ban_user.id, permissions)
            await message.answer(f"{ban_user.full_name} endi yoza oldi.")
        else:
            await message.answer("Kimnidur mutedan olish uchun siz userni hxabariga replay qilishingiz kerak")
    else:
        await message.reply("Siz gruhda admin emsiz foydalanuchilarni mutedan olish uchun.")
