from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.inline.common.keyboards import create_back_button
from src.keyboards.inline.user.callbacks import AdvertisementCallbackFactory, ProfileCallbackFactory


def create_profile_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Мои объявления',
            callback_data=ProfileCallbackFactory(action='my_advertisement').pack(),
        )
    )

    return builder.as_markup()


def create_detail_advertisement_keyboard(advertisement_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Откликнуться',
            callback_data=AdvertisementCallbackFactory(action='respond', advertisement_id=advertisement_id).pack(),
        ),
    )
    builder.row(
        *create_back_button(),
    )

    return builder.as_markup()
