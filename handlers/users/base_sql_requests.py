from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import AdminDelete
from keyboards import kb_confirmation
from aiogram.dispatcher.filters import Command

from SQL.wrk_db import get_admins, delete_admin, get_list_tables


@dp.message_handler(Command("get_admins"))
async def command_getId(message: types.Message):
    await message.answer(f"Admins in table:\n\n {get_admins()}")


@dp.message_handler(Command("get_list_tables"))
async def command_getId(message: types.Message):
    await message.answer(f"Admins in table:\n\n {get_list_tables}")



@dp.message_handler(Command("delete_admin"))
async def delete_admin(message: types.Message):
    await message.answer(f"Введите id админа которого хотите удалить:\n\n {get_admins()}")
    await AdminDelete.getID.set()


@dp.message_handler(state=AdminDelete.getID)
async def get_id_delete_admin(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обчное состояние")
        await state.finish()
        return

    await state.update_data(getID=answer)

    await message.answer(f'Вы уверены, что хотите удалить админа с id: {answer}?', reply_markup=kb_confirmation)

    await AdminDelete.confirmation.set()


@dp.message_handler(state=AdminDelete.confirmation)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "Подтвердить":
        data = await state.get_data()
        admin_id = data.get("getID")

        delete_admin(admin_id)

        await message.answer(f"Вы удалили админа с id: {admin_id}")
        await state.finish()

    elif answer == "/cancel":
        await message.answer("вы вернулись в обчное состояние")
        await state.finish()
        return


