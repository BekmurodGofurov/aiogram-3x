from aiogram.utils.keyboard import InlineKeyboardBuilder
from calendar import Calendar
kalendar = Calendar().itermonthdays2(year=2024, month=8)

inline_builder = InlineKeyboardBuilder()

for i in ("Du","Se","Ch","Pa", "Ju","Sh", "Ya"):
    inline_builder.button(text=i, callback_data=i)

for i in kalendar:
    if i[0]: inline_builder.button(text=f"{i[0] : 02}", callback_data=f"{i[0] : 02}")
    else: inline_builder.button(text=" ", callback_data="null")

inline_builder.adjust(7, repeat=True)
inline_builder = inline_builder.as_markup()





