from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_confirmation = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Подтвердить'),
            KeyboardButton('Отменить')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
