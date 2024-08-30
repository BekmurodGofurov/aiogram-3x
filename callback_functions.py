from aiogram.types import CallbackQuery

async def day(query: CallbackQuery):
    data =  query.data
    if data == "null": await query.answer(text="Bu boshliq boshqa oyga tegishli", show_alert=False)
    if data == "Du": await query.answer(text="Haftaning Duyshanba kunlari", show_alert=False)    
    if data == "Se": await query.answer(text="Haftaning Seyshanba kunlari", show_alert=False)    
    if data == "Ch": await query.answer(text="Haftaning Chorshanba kunlari", show_alert=False)    
    if data == "Pa": await query.answer(text="Haftaning Payshanba kunlari", show_alert=False)    
    if data == "Ju": await query.answer(text="Haftaning Juma kunlari", show_alert=False)    
    if data == "Sh": await query.answer(text="Haftaning Shanba kunlari", show_alert=False)    
    if data == "Ya": await query.answer(text="Haftaning Yakshanba kunlari", show_alert=False)    
    await query.answer(text=f"{data}-kun bo'yicha ma'lumot yo'q", show_alert=True)