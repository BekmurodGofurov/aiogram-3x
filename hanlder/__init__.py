from aiogram import Router
from . import groups
from . import users

router = Router()
router.include_routers(groups.group_router, users.user_router)