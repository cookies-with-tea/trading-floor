from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto

from src.keyboards.inline.common.callbacks import CategoryCallbackFactory, MenuCallbackFactory, UrgencyCallbackFactory
from src.keyboards.inline.common.keyboards import (
    create_back_menu_keyboard,
)
from src.models.media import InputMediaGroup
from src.services.api.advertisement.service import AdvertisementAPIService
from src.utils.formatting import format_detail_advertisement, format_list_advertisement
from src.misc.states import CreateAdvertisement, SelectAdvertisement
from src.utils.validatiors import str_to_int

router = Router()

advertisement_service: AdvertisementAPIService = AdvertisementAPIService.get_instance()


@router.callback_query(MenuCallbackFactory.filter(F.action == 'list_advertisement'))
async def list_advertisement(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(SelectAdvertisement.select)
    advertisements = format_list_advertisement(await advertisement_service.get_all_advertisement())

    await callback.message.edit_text(
        'Пожалуйста, введите номер объявления:\n' + advertisements,
        reply_markup=create_back_menu_keyboard(),
    )
    await callback.answer()


@router.message(StateFilter(SelectAdvertisement.select))
async def detail_advertisement(message: types.Message, state: FSMContext) -> None:
    advertisement_id = str_to_int(message.text)
    if advertisement_id is None:
        await message.answer('Номер должен быть числом')
        return

    advertisement = await advertisement_service.get_advertisement_by_id(advertisement_id)
    if advertisement.images:
        media = InputMediaGroup()
        for file in advertisement.images:
            media.photos.append(
                InputMediaPhoto(
                    type='photo',
                    media=FSInputFile(file.url),
                )
            )
        await message.answer_media_group(media.to_line_list())

    await message.answer(
        format_detail_advertisement(advertisement),
        reply_markup=create_back_menu_keyboard(),
    )
    await state.clear()
