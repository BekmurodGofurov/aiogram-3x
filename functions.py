from aiogram import Bot
from aiogram.types import  Message
from aiogram.fsm.context import FSMContext
from data import users, get_user_ball
from states import get_user_real_name
from keyboards import main_menu

async def start_command_answer(message: Message, state: FSMContext, bot: Bot):
  if message.text[7:].isdigit():
    if users.get(str(message.from_user.id)):
      if int(message.text[7:]) == message.from_user.id: await message.answer(F"Siz o'zingizga o'zingiz referal bo'la olmaysiz")
      else: await message.answer(f"Siz referal bo'lgansiz")
    else:
      reffer_id = message.text[7:]
      users[str(message.from_user.id)] = {"reffer_id": reffer_id, "flag": False}
      await bot.send_message(reffer_id, F"{message.from_user.full_name} sizga referal bo'ldi.")
      await state.set_state(get_user_real_name.name)
      await message.answer(F"Menga haqiqyiy ism-familyangizni yuboring.")
  else:
    if users.get(str(message.from_user.id)):
      await message.answer(f"Siz Asosiy menudasiz.", reply_markup=main_menu)
    else:
      users[str(message.from_user.id)] = {"reffer_id": None, "flag": False}
      await state.set_state(get_user_real_name.name)
      await message.answer(F"Menga haqiqyiy ism-familyangizni yuboring.")

async def get_realy_name_answer(message: Message, state: FSMContext):
  users[str(message.from_user.id)]["real_name"] = message.text
  users[str(message.from_user.id)]["flag"] = True
  await message.answer(f"{message.text} sizni eslab qoldim!", reply_markup=main_menu)
  await state.clear()

async def get_rf_id_answer(message: Message, state: FSMContext):
  if users.get(str(message.from_user.id)):
    ref_link = f"https://t.me/python_000_bot?start={message.from_user.id}"
    await message.answer(f"Sizni refferal havolangiz: \n\n{ref_link}")
  else:
    users[str(message.from_user.id)] = {"reffer_id": None, "flag": False}
    await state.set_state(get_user_real_name.name)
    await message.answer(F"Menga haqiqyiy ism-familyangizni yuboring.")
    
async def get_user_ball_answer(message: Message, state: FSMContext):
  if users.get(str(message.from_user.id)):
    user_ball = get_user_ball(str(message.from_user.id))
    await message.answer(f"Sizni ballingiz: {user_ball}")
  else:
    users[str(message.from_user.id)] = {"reffer_id": None, "flag": False}
    await state.set_state(get_user_real_name.name)
    await message.answer(F"Menga haqiqyiy ism-familyangizni yuboring.")
  user_ball = get_user_ball(message.from_user.id)
  