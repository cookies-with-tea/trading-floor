from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.inline.user.callbacks import ProfileCallbackFactory


def create_profile_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Мои объявления',
            callback_data=ProfileCallbackFactory(action='my_advertisement').pack(),
        )
    )

    return builder.as_markup()
