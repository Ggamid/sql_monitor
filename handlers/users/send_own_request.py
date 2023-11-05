from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import OwnRequest
from SQL.wrk_db import sent_own_requets
from keyboards import kb_confirmation

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("sent_own_request"))
async def command_getId(message: types.Message):
    await message.answer(f"Пришлите текст собственного запроса")
    await OwnRequest.getText.set()


@dp.message_handler(state=OwnRequest.getText)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обычное состояние")
        await state.finish()
        return

    await state.update_data(getText=answer)

    await message.answer(f'Вы уверены, что хотите отправить этот запрос? \n {answer}', reply_markup=kb_confirmation)

    await OwnRequest.confirmation.set()


@dp.message_handler(state=OwnRequest.confirmation)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "Подтвердить":
        data = await state.get_data()
        request = data.get("getText")
        await message.answer(f"ваш запрос вернул: \n {sent_own_requets(request)}")
        await state.finish()

    elif answer in ["/cancel", "Отменить"]:
        await message.answer("вы отменили создание новой таблицы")
        await state.finish()
        return