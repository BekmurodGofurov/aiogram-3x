from aiogram.types import Message

async def new_members_answer(message: Message):
    new_members = message.new_chat_members[0]
    await message.answer(f"Assalomu alekum, {new_members.full_name}!")
    await message.delete()