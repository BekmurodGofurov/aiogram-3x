from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ok", callback_data="ok")
    ]
])