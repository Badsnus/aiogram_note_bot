from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_note_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('✅ Создать', callback_data='add_note')
    ],
    [
        InlineKeyboardButton(
            '🔙 Вернуться назад',
            callback_data='note_add_description'
        )
    ],
    [
        InlineKeyboardButton('❌ Отменить', callback_data='cancel_note')
    ]
])


def get_note_keyboard(prev_state: str = None) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    if prev_state is not None:
        markup.row(
            InlineKeyboardButton(
                '🔙 Вернуться назад',
                callback_data=f'note_add_{prev_state}'
            )
        )
    markup.row(
        InlineKeyboardButton(
            '❌ Отменить создание',
            callback_data='note_add_STOP'
        )
    )
    return markup
