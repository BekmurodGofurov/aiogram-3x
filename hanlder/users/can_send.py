from aiogram import Bot
from aiogram.types import Message, ChatPermissions

async def on_command_answer(message: Message):
    permissions = ChatPermissions(can_send_messages=True)
    await message.chat.set_permissions(permissions)
    await message.answer(f"Groupda endi hamma yoza oldi.")
    
async def off_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ["administrator", "creator"]:
        permissions = ChatPermissions(can_send_messages=False)
        await message.chat.set_permissions(permissions)
        await message.answer(f"Endi Groupda oddiy userlar yoza olmaydi!")
    else:
        await message.answer(f"Siz grouda yozishni cheklay olmaysiz buning uchun siz admin bo'lishnigiz kerak")