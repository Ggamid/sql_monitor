from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import TruncateData
from keyboards import kb_confirmation
from aiogram.dispatcher.filters import Command

from SQL.wrk_db import get_list_tables, drop_data_in_table


@dp.message_handler(Command("truncate_data"))
async def delete_admin(message: types.Message):
    await message.answer(f"Введите название таблицы данные в которой вы хотите безвозвратно удалить:\nДоступные таблицы:👇🏻\n\n{get_list_tables()}")
    await TruncateData.getTable.set()
    return


@dp.message_handler(state=TruncateData.getTable)
async def get_id_delete_admin(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обчное состояние")
        await state.finish()
        return

    await state.update_data(getTable=answer)

    await message.answer(f'Вы уверены, что хотите удалить все данные из таблицы: {answer}?', reply_markup=kb_confirmation)

    await TruncateData.confirmation.set()
    return


@dp.message_handler(state=TruncateData.confirmation)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "Подтвердить":
        data = await state.get_data()
        table = data.get("getTable")

        drop_data_in_table()

        await message.answer(f"Вы удалили все данные из таблицы: {table}")
        await state.finish()
        return

    elif answer == "/cancel":
        await message.answer("вы вернулись в обчное состояние")
        await state.finish()
        return
