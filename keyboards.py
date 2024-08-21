from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

reply_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 - button"),
            KeyboardButton(text="2 - button"),
            KeyboardButton(text="3 - button"),
        ],
        [
            KeyboardButton(text="4 - button"),
            KeyboardButton(text="5 - button"),
            KeyboardButton(text="6 - button"),
        ]
    ], resize_keyboard=True,
    is_persistent=False, # For not allow to hide button
    one_time_keyboard=False, #Hide buttons after sent text
    input_field_placeholder="Bro, Bosing😜"
)
