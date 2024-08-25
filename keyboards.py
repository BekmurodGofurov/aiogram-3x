from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

test_for_markup = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="Kontakni yuborish", request_contact=True),
    KeyboardButton(text="Joylashuvni yuborish", request_location=True)
  
  ]
],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder="Tugmalrdan birni tanlang!"
)
