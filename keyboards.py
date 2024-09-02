from aiogram.utils.keyboard import InlineKeyboardBuilder

cal_builder = InlineKeyboardBuilder()

for i in "CD789-456+123*.0/=":
    cal_builder.button(text=i, callback_data=i)

cal_builder.adjust(2,4, repeat=False)

cal_builder = cal_builder.as_markup()
