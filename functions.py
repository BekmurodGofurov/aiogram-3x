from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import newAplication


# async  def get_user_info(message: Message, bot: Bot):
#     user = await bot.get_chat(message.from_user.id)
#     user_photos = await bot.get_user_profile_photos(user.id)
#     matn = f"{message.from_user.mention_html('USER')} INFO:\n\nIsm-Familya: {message.from_user.full_name}\nID: {message.from_user.id}\n"

#     if user.bio: matn += f"Bio: {user.bio}\n"
#     if user.username : matn += f"Username: @{user.username}\n"
#     if user_photos.photos:
#         await message.answer_photo(user_photos.photos[0][-1].file_id, caption=matn, parse_mode="HTML")
#     else:
#         await message.answer(matn, parse_mode="HTML")

# async def start_answer(message: Message, bot:Bot, state: FSMContext):
#     # await bot.send_message(message.from_user.id, f"Salom {message.from_user.mention_html(f'{message.from_user.first_name}')}", parse_mode="HTML")        
#     await message.answer("Salom, Ismingizni yuboring")
#     await state.set_state(sign_up.name)


# async def help_answer(message: Message, bot: Bot):
#     matn = f"""
#     <b>Bot buyriqlari:</b>

#     /start - Botni ishga tushirish
#     /help - Yordam olish!
# """
#     await bot.send_message(message.from_user.id, matn, parse_mode="HTML")    

# async def sign_up_name(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer(f"Ismingizni oldim {message.text}")
#     await message.answer(f"Yoshingizni yuboring")

#     await state.set_state(sign_up.age)


# async def sign_up_age(message: Message, bot: Bot, state: FSMContext):
#     data = await state.get_data()
#     await message.answer(f"""Ma'lumotlaringiz
#     Ismingiz: {data.get("name")}
#     Yoshingiz: {message.text}""")
#     state.clear


async def start_command_answer(message: Message):
    await message.answer(f"Salom {message.from_user.first_name}\n\nAgar botdan foydalanishni bilmasangiz /help commandasini yuboring.")


async def help_answer(message: Message):
    matn = """Botdan foydalanish:
    /new - yangi ariza yuborish
    /stop - joriy yuborilayotkan arizani bekor qilsih.
    """
    await message.answer(matn)

async def new_answer(message: Message, state: FSMContext):
    await message.answer("Menga ism-familyangizni yuboring!")
    await state.set_state(newAplication.name)

async def stop_answer(message: Message, state: FSMContext):
    this_state= await state.get_state()
    if this_state == "none": await message.answer("Bekor qilish uchun sizda ariza mavjud emas!")
    else: 
        await state.clear()
        await message.answer("Joriy ariza bekor qilindi!")

async def newAplication_name_answer(message: Message, state: FSMContext):
    if len(message.text.split()) == 2:
        if not ("0" in message.text or
                "1" in message.text or
                "2" in message.text or
                "3" in message.text or
                "4" in message.text or
                "5" in message.text or
                "6" in message.text or
                "7" in message.text or
                "8" in message.text or
                "9" in message.text):
            await state.update_data(name=message.text)
            await message.answer(f"Ism-familyangiz qabul qilindi\n\n{message.text}")
            await message.answer("Yoshingizni yuboring!")
            await state.set_state(newAplication.age)
        else: await message.answer("Ism-familyada raqam qatnashishi mumkun emas!")
    else: await message.answer("Ism-familyangizni to'g'ri va to'liq yozing!")

async def newAplication_age_answer(message: Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 100 and int(message.text) > 10:
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qanul qilindi. \n\n{message.text}")
            await message.answer("Menga telefon raqamingizni yuboring!")
            await state.set_state(newAplication.phone)
        else: await message.answer("Uzir sizni yoshingiz bizaga to'gri kelmaydi!")
    else: await message.answer("Yoshingizni yuborish uchun faqat raqamdan foydalaning!")        

async def newAplication_phone_answer(message: Message, state: FSMContext):
    if message.text.isdigit():
        if len(message.text) == 9 or len(message.text) == 12:
            await state.update_data(phone=message.text)
            await message.answer(f"Telefon raqamingiz qabul qilndi. \n\n{message.text}")
            await message.answer("Kasbingiz nima?")
            await state.set_state(newAplication.job)
        else: await message.answer("telefon raqamni shu ko'rinishda kiriting 123456789 yoki 998123456789!")
    else: await message.answer("Telefon raqamni yuborish uchun faqat raqamdan foydalaning!")    

async def newAplication_job_answer(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(job=text)
    await message.answer(f"Kasibingiz qabul qilndi. \n\n{text}")
    await message.answer("Maqsadingiz nima?")
    await state.set_state(newAplication.goal)

async def newAplication_goal_answer(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(goal=text)
    data = await state.get_data()
    ariza = (f"Ariza beruvchi: {data.get('name')}\n"
             f"Yoshi: {data.get('age')}\n"
             f"Telefon raqami: {data.get('phone')}\n"
             f"Kasbi: {data.get('job')}\n"
             f"Maqsadi: {data.get('goal')}\n")
    await message.answer(f"Sizni arizangizni yubora veraylikmi \n\n{ariza}\n\nIltimos Ha yoki /stop deb javob bering!")    
    await state.set_state(newAplication.verify)

async def newAplication_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        ariza = (f"Ariza beruvchi: {data.get('name')}\n"
                f"ID: {message.from_user.id}\n" 
                f"Yoshi: {data.get('age')}\n"
                f"Telefon raqami: {data.get('phone')}\n"
                f"Username: @{message.from_user.username}\n"
                f"Kasbi: {data.get('job')}\n"
                f"Maqsadi: {data.get('goal')}\n")
        await bot.send_message(5841656536, ariza)
        await message.answer("Siznig arizangiz adminga yuborildi.")    
        await state.clear()
    else:
        await message.answer("Arizani yuborish uchun yoki rad etish uchun Ha yoki /stop dan foydalaning!")