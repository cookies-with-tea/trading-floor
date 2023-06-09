from aiogram import types
from aiogram.fsm.context import FSMContext

from src.keyboards.inline.common.keyboards import create_menu_keyboard


async def start(message: types.Message, state: FSMContext, is_edit: bool = False):
    message_method = message.edit_text if is_edit else message.answer

    await message_method(
        text='Доброй пожаловать в бота для торговой площадки ВКИ.\n\nПожалуйста, выберите действие:',
        reply_markup=create_menu_keyboard(),
    )
    await state.clear()
