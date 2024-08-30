from aiogram.types import CallbackQuery


async def ok_action(query: CallbackQuery):
    await query.answer("Xambar o'childi.", show_alert=False)

    await query.message.delete()