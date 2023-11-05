from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.states import Register
from aiogram.dispatcher.filters import Command
from keyboards import kb_confirmation, access_level
from SQL.wrk_db import reg_admin


@dp.message_handler(Command("add_admin"))
async def command_getId(message: types.Message):
    await message.answer(f"Пришлите telegram id нового администратора")
    await Register.get_ID.set()


@dp.message_handler(state=Register.get_ID)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обычное состояние")
        await state.finish()
        return


    await state.update_data(get_ID=answer)


    await message.answer('Отправьте уровень доступа админа: "Senior", "Midle", "Junior"', reply_markup=access_level)

    await Register.get_access_level.set()


@dp.message_handler(state=Register.get_access_level)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(get_access_level=answer)

    if answer == "/cancel":
        await message.answer("вы вернулись в обычное состояние")
        await state.finish()
        return

    data = await state.get_data()
    id = data.get("get_ID")
    acces_level = data.get('get_access_level')

    await message.answer(f'Отлично! вы хотите добавить админа с id: {id} и acces_level{acces_level}?',
                         reply_markup=kb_confirmation)

    await Register.confirmation.set()


@dp.message_handler(state=Register.confirmation)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    data = await state.get_data()
    id = data.get("get_ID")
    access_level = data.get('get_access_level')



    if answer == "Подтвердить":
        reg_admin(tg_id=id, acces_level=access_level)
        await message.answer(f'Отлично! вы добавили админа с id: {id} и acces_level: {access_level}?')
        await state.finish()
        return

    else:
        await message.answer("вы отменили добавление админа")
        await state.finish()
        return

