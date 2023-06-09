from aiogram import types
from aiogram.fsm.context import FSMContext

from src.keyboards.inline.common.keyboards import create_menu_keyboard


async def start(message: types.Message, state: FSMContext):
    await message.answer(
        text='Доброй пожаловать в бота для торговой площадки ВКИ.\n\nПожалуйста, выберите действие:',
        reply_markup=create_menu_keyboard(),
    )
    await state.clear()
