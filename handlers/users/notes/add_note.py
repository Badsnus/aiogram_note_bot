from aiogram import types, dispatcher

from loader import dp, Note, User
from states import NoteState
from keyboards.inline import add_note_menu, get_note_keyboard

states_dict = {'name': (NoteState.first, 'имя', None),
               'description': (NoteState.description.set, 'описание', 'name')}


def remove_buttons_decorator(func):
    async def wrapper(*args, **kwargs):
        message = (await kwargs['state'].get_data()).get('message')
        await message.edit_reply_markup(types.InlineKeyboardMarkup())
        return await func(*args, **kwargs)

    return wrapper


@dp.callback_query_handler(text_startswith='note_add_', state='*')
async def change_state(call: types.CallbackQuery,
                       state: dispatcher.FSMContext):
    data = states_dict.get(call.data.split('_')[2], 'STOP')
    if data == 'STOP':
        await state.finish()
        return await call.message.edit_text('Создание задачи отменено')
    await data[0]()
    await call.message.edit_text(f'Введите {data[1]} для задачи',
                                 reply_markup=get_note_keyboard(data[2]))


@dp.message_handler(text='Добавить задачу')
async def ask_note_name(message: types.Message, state: dispatcher.FSMContext):
    m = await message.answer('Введите имя для задачи',
                             reply_markup=get_note_keyboard())
    await NoteState.first()
    await state.update_data(message=m)


@dp.message_handler(state=NoteState.name)
@remove_buttons_decorator
async def ask_note_desc(message: types.Message, state: dispatcher.FSMContext,
                        **kwargs):
    m = await message.answer('Введите описание задачи',
                             reply_markup=get_note_keyboard('name'))
    await state.update_data({
        'name': message.text,
        'message': m
    })
    await NoteState.next()


@dp.message_handler(state=NoteState.description)
@remove_buttons_decorator
async def ask_note_verd(message: types.Message, state: dispatcher.FSMContext,
                        **kwargs):
    data = await state.get_data()
    m = await message.answer(f'''
Ваша задача: <b>{data.get('name')}</b>
    
Описание задачи:
<code>{message.text}</code>

<b>Создать задачу?</b>''',
                             reply_markup=add_note_menu
                             )
    await state.update_data({
        'description': message.text,
        'message': m
    })
    await NoteState.next()


@dp.callback_query_handler(state=NoteState.create)
async def do_verdict(call: types.CallbackQuery, state: dispatcher.FSMContext):
    data = await state.get_data()
    await state.finish()
    if call.data == 'cancel_note':
        return await call.message.edit_text('Отменил создание задачи')
    await Note.objects.create(
        user=await User.objects.get(user_id=call.from_user.id),
        name=data.get('name'),
        description=data.get('description')
    )
    await call.message.edit_text('Задача создана')
