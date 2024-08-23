from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

main_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Refferal havola"),
            KeyboardButton(text="Mening ballarim"),
        ]
    ], resize_keyboard=True,
    is_persistent=True,
    one_time_keyboard=True,
    input_field_placeholder="Main Manu"
)
