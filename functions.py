from aiogram.types import Message

async def get_info(message: Message):
    await message.answer(f"""
Chat turi: {message.chat.type}\n
Chat nomi: {message.chat.title}\n
Chat ID: {message.chat.id}""")
    
async def new_chat_members_answer(message: Message):
    for member in message.new_chat_members:
        await message.answer(text=f"Salom {member.full_name}, botga xushkelibsiz.")
    await message.delete()        

async def left_chat_member_answer(message: Message):
    await message.answer(text=F"Yaxshi boring {message.left_chat_member.full_name}")
    await message.delete()  