from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, User
from keyboards.default import main_menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await User.objects.get_or_create(
        {}, user_id=message.from_user.id
    )
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Этот бот поможет тебе записывать все свои мысли.",
        reply_markup=main_menu
    )
