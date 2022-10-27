from aiogram import types

from loader import dp, User, Note
from keyboards.inline import get_note_list_menu, get_note_detail_menu


async def get_note_list_text_and_keyboard(user_id: int) -> (
        tuple[str, types.InlineKeyboardMarkup]):
    notes = await Note.objects.filter(
        user__user_id=user_id,
        completed=False
    ).all()
    return "Ваши задачи", get_note_list_menu(notes)


@dp.message_handler(text='Мои задачи')
async def show_note_list(message: types.Message):
    text, markup = await get_note_list_text_and_keyboard(message.from_user.id)

    await message.answer(
        text,
        reply_markup=markup
    )


@dp.callback_query_handler(text='note_list')
async def show_note_list_call(call: types.CallbackQuery):
    text, markup = await get_note_list_text_and_keyboard(call.from_user.id)

    await call.message.edit_text(
        text,
        reply_markup=markup
    )


@dp.callback_query_handler(text_startswith='note_detail-')
async def show_note(call: types.CallbackQuery):
    data = call.data.split('-')[1:]
    note = await Note.objects.first(id=int(data[0]))
    if not note:
        return await call.message.edit_text('Эта задача не найдена')
    text = (f'Задача: <b>{note.name}</b>\n\n'
            f'Описание задачи:\n<code>{note.description}</code>\n\n'
            f'Задача создана: <b>{str(note.date)[:19]}</b>')
    await call.message.edit_text(text,
                                 reply_markup=get_note_detail_menu(data[0]))


@dp.callback_query_handler(text_startswith='note_did-')
async def mark_note_completed(call: types.CallbackQuery):
    await call.answer('Задача выполнена')
    note = await Note.objects.first(id=int(call.data.split('-')[1]))
    if note:
        await note.update(completed=True)
    await show_note_list_call(call)
