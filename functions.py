from aiogram import Bot
from aiogram.types import  Message
from keyboards import  test_for_markup

async def start_command_reply(message: Message):
  await message.reply(f"Salom {message.from_user.full_name}\nIltimos tugmalardan birini tanlang!", reply_markup=test_for_markup)

async def get_contact_info(message: Message):
  contact_info = f"""
--------------------
Ism-Familya: {message.contact.first_name} {message.contact.last_name}\n
--------------------
User ID: {message.contact.user_id}\n
--------------------
Telefon raqam: {message.contact.phone_number}\n
--------------------
"""
  await message.reply(f"Kontakt qabul qilindi.\n" + contact_info)
  
async def get_location_info(message: Message):
  location_info = f"""
-------------------
Kenglik: {message.location.latitude}
-------------------
Uzunlik: {message.location.longitude}
-------------------
"""
  await message.reply("Joylashuv qabul qilindi." + location_info)