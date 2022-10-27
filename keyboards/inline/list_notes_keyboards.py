from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_note_list_menu(notes: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    for note in notes:
        markup.insert(
            InlineKeyboardButton(f'Задача: {note.name}',
                                 callback_data=f'note_detail-{note.id}')
        )
    return markup


def get_note_detail_menu(note_id: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('✅ Задача выполнена',
                                 callback_data=f'note_did-{note_id}')
        ],
        [
            InlineKeyboardButton('🔙 Вернуться назад',
                                 callback_data=f'note_list')
        ]
    ])

    return markup
