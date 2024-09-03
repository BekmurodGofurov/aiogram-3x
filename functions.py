from aiogram.types import Message, ChatPermissions

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

async def mute_member_answer(message: Message):
    user_id = message.reply_to_message.from_user.id
    permission = ChatPermissions(can_send_message=False)
    await message.chat.restrict(user_id, permission)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} yozishdan mahrum qilindi!", parse_mode='HTML')

async def unmute_member_answer(message: Message):
    user_id = message.reply_to_message.from_user.id
    permission = ChatPermissions(can_send_message=True,can_invite_users=True,can_send_media_messages=True,can_send_other_messages=False,)
    await message.chat.restrict(user_id, permission)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} endi yoza olsiz!", parse_mode='HTML')

async def ban_member_answer(message: Message):
    user_id = message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} Gruhdan haydaldi", parse_mode='HTML')

async def unban_member_answer(message: Message):
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} Blockdan ozod qilindi", parse_mode='HTML')