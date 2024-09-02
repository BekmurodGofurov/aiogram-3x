from aiogram.types import Message
import keyboards

async def open_calculator_answer(message: Message):
    await message.reply(text=f"|", reply_markup=keyboards.cal_builder)