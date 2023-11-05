from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import CreateTable
from keyboards import kb_confirmation
from SQL.wrk_db import create_table_with_bot
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("create_table"))
async def create_table(message: types.Message):
    await message.answer("Данная команда позовлит вам создать таблицу со столбцами имеющими тип данных varchar(255)"
                         "\n\nПришлите имя для новой таблицы ✍🏻")
    await CreateTable.getNameTable.set()


@dp.message_handler(state=CreateTable.getNameTable)
async def get_table_name(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обычное состояние")
        await state.finish()
        return

    await message.answer("Пришлите названия столбцов для таблицы в формате: \n\n"
                         "name phonenumber tg_id email")

    await state.update_data(getNameTable=answer)

    await CreateTable.getColumns.set()


@dp.message_handler(state=CreateTable.getColumns)
async def get_table_name(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "/cancel":
        await message.answer("вы вернулись в обычное состояние")
        await state.finish()
        return
    await state.update_data(getColumns=answer)

    data = await state.get_data()
    table_name = data.get("getNameTable")
    columns = data.get("getColumns")

    await message.answer(f"Подтвердить создание таблицы с именем '{table_name}' и "
                         f"столбцами: \n\n {columns} ", reply_markup=kb_confirmation)

    await CreateTable.confirmation.set()


@dp.message_handler(state=CreateTable.confirmation)
async def command_getId(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "Подтвердить":

        data = await state.get_data()
        table_name = data.get("getNameTable")
        columns = data.get("getColumns")

        await message.answer(f"Таблица создана: \n \n"
                             f"{create_table_with_bot(table_name, list(columns.split()))}")
        await state.finish()

    elif answer in ["/cancel", "Отменить"]:
        await message.answer("вы вернулись в обчное состояние")
        await state.finish()
        return
