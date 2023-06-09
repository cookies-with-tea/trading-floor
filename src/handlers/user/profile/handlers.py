from aiogram import F, Router, types
from aiogram.types import FSInputFile

from src.keyboards.inline.common.callbacks import MenuCallbackFactory
from src.keyboards.inline.common.keyboards import create_back_menu_keyboard
from src.services.api.user.service import UserAPIService
from src.utils.formatting import format_profile

router = Router()

user_service: UserAPIService = UserAPIService.get_instance()


@router.callback_query(MenuCallbackFactory.filter(F.action == 'profile'))
async def my_profile(callback: types.CallbackQuery):
    user = await user_service.get_user_by_id(1)

    if user.avatar:
        image = FSInputFile(user.avatar, filename='people.jpg')
        await callback.message.answer_photo(image)
        await callback.message.answer(format_profile(user), reply_markup=create_back_menu_keyboard())
    else:
        await callback.message.edit_text(format_profile(user), reply_markup=create_back_menu_keyboard())

    await callback.answer()
