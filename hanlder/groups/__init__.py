from aiogram import Router, F
from aiogram.filters.command import Command
from . import new_member
from . import left_member
from . import ban
from . import mute

group_router = Router()

group_router.message.register(new_member.new_members_answer, F.new_chat_members)
group_router.message.register(left_member.left_member_answer, F.left_chat_member)
group_router.message.register(ban.ban_command_answer, Command("ban"))
group_router.message.register(ban.unban_command_answer, Command("unban"))
group_router.message.register(mute.mute_command_answer, Command("mute"))
group_router.message.register(mute.unmute_command_answer, Command("unmute"))