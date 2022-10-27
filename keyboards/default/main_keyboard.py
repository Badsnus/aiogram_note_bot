from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('Добавить задачу'),
        KeyboardButton('Мои задачи')
    ],
])
