from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class sign_up(StatesGroup):
    name=State()
    age=State()