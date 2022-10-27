from aiogram.dispatcher.filters.state import State, StatesGroup


class NoteState(StatesGroup):
    name = State()
    description = State()
    create = State()
