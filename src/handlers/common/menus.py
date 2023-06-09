from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from src.handlers.user.start import start
from src.keyboards.inline.common.callbacks import MenuCallbackFactory


router = Router()


@router.callback_query(MenuCallbackFactory.filter(F.action == 'back'))
async def go_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await start(callback.message, state, is_edit=True)
