from aiogram import Router, F
from aiogram.filters import CommandStart
from . import start
from . import reklama
from . import can_send
import filters

user_router = Router()
user_router.message.register(start.start, CommandStart())
user_router.message.register(reklama.get_ads_answer, filters.ads.isAd())
user_router.message.register(can_send.on_command_answer, F.text=="/on")
user_router.message.register(can_send.off_command_answer, F.text=="/off")
