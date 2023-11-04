from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

access_level = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Senior'),
            KeyboardButton('Midle'),
            KeyboardButton('Junior')

        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
