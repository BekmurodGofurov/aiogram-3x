from aiogram.types import Message

async def left_member_answer(messag: Message):
    left_member = messag.left_chat_member
    await messag.answer(f"Yaxshi boring {left_member.full_name}")
    await messag.delete()