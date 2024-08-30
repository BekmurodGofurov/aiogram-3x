from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

builder = ReplyKeyboardBuilder()
# builder.button(text="1 button")
# builder.button(text="3 button")

# builder.add(
#   KeyboardButton(text="4 button"),
#   KeyboardButton(text="5 button"),
#   KeyboardButton(text="6 button")
# )

# builder.row(
#   KeyboardButton(text="4 button"),
#   KeyboardButton(text="5 button"),
#   KeyboardButton(text="6 button"),
#   KeyboardButton(text="7 button"),
#   KeyboardButton(text="8 button"),
#   KeyboardButton(text="9 button"),
#   KeyboardButton(text="10 button"),
#   KeyboardButton(text="11 button"),
#   KeyboardButton(text="12 button"),
#   width=4
# )

for i in range(50):
    builder.button(text=f"{i+1}-Tugma")

builder.adjust(1, 2, 3, 4, 3, 2, repeat=True)    

builder = builder.as_markup()

builder.resize_keyboard = True
builder.is_persistent = True
builder.one_time_keyboard = False
